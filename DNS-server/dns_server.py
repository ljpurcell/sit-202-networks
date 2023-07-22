from socket import socket, AF_INET, SOCK_DGRAM

HOST = "127.0.0.1"
PORT = 8080

def get_transaction_id(id_bytes):
    tid = ""
    for byte in id_bytes[:2]: # first two byes are the TID
        tid += hex(byte)[2:] # strip leading hexcode
    return tid

def get_flags(flag_bytes):
    byte1 = flag_bytes[:1]
    byte2 = flag_bytes[1:]

    # BYTE 1
    QR = "1" 
    OPCODE = ""
    for bit_shift in range(6, 3, -1):
        OPCODE += "1" if ord(byte1) & (1 << bit_shift) else "0"
    AA = "0"
    TC = "0"
    RD = "1" if ord(byte1) & 1 else "0"
    r_byte1 = int(QR + OPCODE + AA + TC + RD, 2).to_bytes(1, 'big')

    # BYTE 2
    RA = "0"
    Z = "0"
    AD = "0"
    CD = "0"
    RCODE = "0000"
    r_byte2 = int(RA + Z + AD + CD + RCODE, 2).to_bytes(1, 'big')
    print(r_byte1 + r_byte2)
    return r_byte1 + r_byte2

def build_response(query):
    transaction_id = get_transaction_id(query[:2])
    flags = get_flags(query[2:4])
    # # flags
    # response_code = format(0, '04b') # 0 = no error
    return

# creates a socket that uses UDP
with socket(AF_INET, SOCK_DGRAM) as s:
    s.bind((HOST, PORT)) # associates the socket with a network interface and port
    print(f"Server running on {HOST}:{PORT}...")

    while True:
        query, addr = s.recvfrom(1024)
        if not query:
            break
        response = build_response(query)
        s.sendto(b"Hello back!", addr)


# needs to display when it starts running

# recieves query messages, returns response messages

# must support A and CNAME records

# must support hostname to IP address translation and host aliasing
