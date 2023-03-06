from flask import Flask, url_for, redirect, request, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = "szikretki"
socketio = SocketIO(app)


@app.route("/")
def home():
    return render_template('index.html')


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)


if __name__ == "__main__":
    socketio.run(app, debug=True)
