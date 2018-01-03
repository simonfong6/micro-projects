"""
server.py
Playing with frontend and backend sockets.
"""

from flask import Flask, send_file
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# SOCKETS----------------------------------------------------------------------
@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    
@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    
@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json['data']))

# WEB PAGES--------------------------------------------------------------------
@app.route('/')
def index():
    return send_file('index.html')

if(__name__ == '__main__'):
    socketio.run(app)
