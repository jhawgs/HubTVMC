# app.py (on Raspberry Pi)
from flask import Flask, render_template, redirect
from flask_socketio import SocketIO, emit
import socket

INTERFACE = ["mineflayer", "uinput"][-1]

if INTERFACE == "uinput":
    from remotecontrol import handle_key
elif INTERFACE == "mineflayer":
    from mineflayer import handle_key
else:
    raise NotImplementedError()

app = Flask(__name__)
socketio = SocketIO(app)

# IP and port of the remote machine to forward events
#REMOTE_IP = '192.168.1.100'  # Change to the target machine's IP
#REMOTE_PORT = 5001

# Set up a socket to send data to the remote machine
remote_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('input_event')
def handle_input_event(data):
    handle_key(data)#print('Received:', data)
    #remote_socket.sendto(str(data).encode(), (REMOTE_IP, REMOTE_PORT))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5022)
