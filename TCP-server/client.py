import socket

SERVER_IP = "127.0.0.1"
PORT = 9876

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((SERVER_IP, PORT))
    sock.sendall(b"I would like to connect")
    data = sock.recv(1024)

print(f"Received back: {data}")
