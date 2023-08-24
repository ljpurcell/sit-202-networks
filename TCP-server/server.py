import socket

IP_ADDRESS = "127.0.0.1"
PORT = 9876

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((IP_ADDRESS, PORT))
    sock.listen()
    print("Listening...")
    conn, addr = sock.accept()
    with conn:
        print(f"Received connection from {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendto(b"Got your message", addr)
