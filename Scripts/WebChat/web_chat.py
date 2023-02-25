from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import datetime

# TODO: Telefonos osszetomorites a konnyebb hasznalhatosag erdekeben

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///messages.db"
app.config["SECRET_KEY"] = "h7f5t8ekh7gw5e3vin985rg723h3oi89ped"
bootstrap = Bootstrap5(app)
db.init_app(app)


class FormMessage(FlaskForm):
    message = StringField("", validators=[DataRequired()], render_kw={'autofocus': True})
    send = SubmitField("Send message")


class FormUsername(FlaskForm):
    username = StringField("", validators=[DataRequired()], render_kw={'autofocus': True})
    submit = SubmitField("Done")


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    sender = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def nickname():
    if request.method == "POST":
        return redirect(url_for('home', username=request.form["username"]))

    return render_template('name.html', form=FormUsername())


@app.route("/<username>")
def home(username):
    messages = db.session.query(Message).all()
    return render_template('index.html', messages=reversed(messages), form=FormMessage(), username=username)


@app.route("/name")
def name():
    return render_template('name.html')


@app.route("/send_message/<username>", methods=["GET", "POST"])
def send_message(username):
    new_record = Message(
        message=request.form["message"],
        time=datetime.datetime.now().replace(microsecond=0),
        sender=username
    )
    db.session.add(new_record)
    db.session.commit()
    return redirect(url_for('home', username=username))


@app.template_filter('format_date')
def format_date_filter(str_date):
    datetime_object = datetime.datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
    return datetime_object.strftime("%B-%d %H:%M")


app.jinja_env.filters['format_date'] = format_date_filter

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
