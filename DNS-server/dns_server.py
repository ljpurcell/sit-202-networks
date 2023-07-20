from socket import socket, AF_INET, SOCK_DGRAM

HOST = "127.0.0.1"
PORT = 8080

# creates a socket that uses UDP
with socket(AF_INET, SOCK_DGRAM) as s:
    s.bind((HOST, PORT)) # associates the socket with a network interface and port
    print(f"Server running on {HOST}:{PORT}...")

    while True:
        data, addr = s.recvfrom(1024)
        if not data:
            break
        print(f"Recieved {data} from {addr}")
        s.sendto(b"Hello back!", addr)


# needs to display when it starts running

# recieves query messages, returns response messages

# must support A and CNAME records

# must support hostname to IP address translation and host aliasing
