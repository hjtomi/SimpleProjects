from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import datetime

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///messages.db"
app.config["SECRET_KEY"] = "h7f5t8ekh7gw5e3vin985rg723h3oi89ped"
bootstrap = Bootstrap5(app)
db.init_app(app)


class FormMessage(FlaskForm):
    message = StringField("", validators=[DataRequired()], render_kw={'autofocus': True})
    send = SubmitField("Send message")


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    sender = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    messages = db.session.query(Message).all()
    form = FormMessage()
    return render_template('index.html', messages=reversed(messages), form=form)


@app.route("/name")
def name():
    return render_template('name.html')


@app.route("/send_message", methods=["GET", "POST"])
def send_message():
    new_message = request.form["message"]
    new_record = Message(
        message=new_message,
        time=datetime.datetime.now().replace(microsecond=0),
        sender="TestUser"
    )
    db.session.add(new_record)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
