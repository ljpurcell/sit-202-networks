from socket import socket, AF_INET, SOCK_DGRAM

HOST = "127.0.0.1" # server's IP address
PORT = 8080 # port being used by the server

# creates a socket that uses UDP
with socket(AF_INET, SOCK_DGRAM) as s:
    s.connect((HOST, PORT)) # connects to the servers socket
    s.sendall(b"Hello, world")
    data = s.recv(1024)
    print(f"Received {data}")
