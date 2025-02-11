# app.py (on Raspberry Pi)
from flask import Flask, render_template, redirect, request
from flask_socketio import SocketIO
import socket
from time import time, sleep

OCCUPIED = False
ACTIVATED = False
REFRESH_TIME = time()
LAST_EVENT_TIME = time()
INTERFACE = ["mineflayer", "uinput", "NONE"][-2]

if INTERFACE == "uinput":
    from remotecontrol import handle_key
elif INTERFACE == "mineflayer":
    from mineflayer import handle_key
elif INTERFACE == "NONE":
    handle_key = lambda x: None
else:
    raise NotImplementedError()

app = Flask(__name__)
socketio = SocketIO(app)

def detect_mobile(user_agent):
    try:
        mobile_keywords = ['Android', 'iPhone', 'iPad', 'Windows Phone', 'Mobile']
        for keyword in mobile_keywords:
            if keyword.lower() in user_agent.lower():
                return True
        return False
    except:
        print("failed mobile detect attempt")
        return False

# IP and port of the remote machine to forward events
#REMOTE_IP = '192.168.1.100'  # Change to the target machine's IP
#REMOTE_PORT = 5001

# Set up a socket to send data to the remote machine
remote_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

@app.route('/')
def index():
    return redirect("waiting-room")#return render_template('index.html'), {"Refresh": "900; url=/waiting-room"}

@app.route('/waiting-room')
def waiting_room():
    global ACTIVATED, LAST_EVENT_TIME
    if not ACTIVATED:
        return redirect("/closed")
    global OCCUPIED
    if time() - LAST_EVENT_TIME >= 120:
        OCCUPIED = False
    print(OCCUPIED)
    if not OCCUPIED:
        print("redirect")
        return redirect("/controller")
    return render_template("waiting.html")

@app.route('/controller')
def controller():
    global ACTIVATED
    if not ACTIVATED:
        return redirect("/closed")
    global REFRESH_TIME, OCCUPIED
    print(OCCUPIED)
    if OCCUPIED:
        return redirect('/waiting-room')
    OCCUPIED = True
    print(OCCUPIED)
    REFRESH_TIME = time()
    if detect_mobile(request.headers.get('User-Agent')):
        return render_template('mobile_index.html')
    else:
        return render_template('index.html')

@app.route('/exit')
def done():
    global ACTIVATED
    if not ACTIVATED:
        return redirect("/closed")
    return render_template('done.html')

@app.route("/override")
def override():
    global ACTIVATED
    if not ACTIVATED:
        return redirect("/closed")
    socketio.emit('force_redirect')
    sleep(5)
    global OCCUPIED
    OCCUPIED = False
    return redirect("/controller")

@app.route("/activate")
def activate():
    global ACTIVATED
    ACTIVATED = True
    print("ACTIVATED")
    return redirect("/controller")

@app.route("/closed")
def inactive_closed():
    return render_template("closed.html")

@socketio.on('input_event')
def handle_input_event(data):
    global LAST_EVENT_TIME
    LAST_EVENT_TIME = time()
    if "dx" not in data:
        print(data)
        handle_key(data)#print('Received:', data)
    elif data["dx"] != 0 or data["dy"] != 0:
        print(data)
        handle_key(data)
    #remote_socket.sendto(str(data).encode(), (REMOTE_IP, REMOTE_PORT))

@socketio.on('disconnect')
def handle_disconnect():
    global OCCUPIED
    OCCUPIED = False

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5022, debug=True, allow_unsafe_werkzeug=True)
