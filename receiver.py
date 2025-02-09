# receiver.py (on the target machine)
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 5001))

print("Listening for events...")

while True:
    data, addr = server_socket.recvfrom(1024)
    print('Received from {}: {}'.format(addr, data.decode()))
