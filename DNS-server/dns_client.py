from socket import socket, AF_INET, SOCK_DGRAM
from secrets import randbits

HOST = "127.0.0.1" # server's IP address
PORT = 8080 # port being used by the server -- make standard DNS port?
QUIT_COMMAND = ":q!"

def build_query(url):
    transaction_id = format(randbits(16), '016b')
    # flags
    qr = 0
    op_code = format(0, '04b')
    recursion_desired = 0

# creates a socket that uses UDP 
with socket(AF_INET, SOCK_DGRAM) as s:
    s.connect((HOST, PORT)) # connects to the servers socket

    more_queries = True

    while more_queries:
        hostname = input("Hostname or alias: ")

        query_message = b""

        s.send(query_message)
        response_message = s.recv(1024)
        print(f"Received {response_message}")

        answer = input(f"Type '{QUIT_COMMAND}' to quit")
        more_queries = answer == QUIT_COMMAND
