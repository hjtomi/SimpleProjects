import time

from flask import Flask, url_for, render_template, redirect
from flask_socketio import SocketIO, send, emit

messages = ['hello', 'whatsup', 'everything is alright', 'great, see you soon']

app = Flask(__name__)
socket = SocketIO(app)
app.config["SECRET_KEY"] = 'dfrtyguhjknkdbhuVYKUJGBDFIUREA4BFOI8Y3UW'


@app.route("/")
def home():
    return render_template('index.html', messages=messages)


@app.route("/button-click")
def button_click():
    messages.append('button pressed')
    return redirect(url_for('home'))


@socket.on('message')
def receive_message(data):
    print(data)
    send(data, broadcast=True)


if __name__ == "__main__":
    socket.run(app, allow_unsafe_werkzeug=True, host='0.0.0.0', port=5000)
