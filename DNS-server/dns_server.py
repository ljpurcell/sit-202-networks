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
    for bit_shift in range(6, 2, -1):
        OPCODE += "1" if ord(byte1) & (1 << bit_shift) else "0" # compares the int ascii value of byte1 to bits 7,6,5 and 4
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

    return r_byte1 + r_byte2

def get_answer_count(answer_bytes):
    domain_part = ""
    domain_parts = []
    bytes_to_go = 0
    getting_part_value = False
    question_type = ""
    for i, byte in enumerate(answer_bytes):

        if getting_part_value:
            bytes_to_go -= 1
            domain_part += chr(byte)
        else:
            bytes_to_go = int(byte) 
            if bytes_to_go < 1:
                question_type = answer_bytes[i+1:i+3] # next two bytes
                break
            getting_part_value = True

        if not bytes_to_go:
            domain_parts.append(domain_part)
            domain_part = ""
            getting_part_value = False

    print(domain_parts)
    print(question_type)

def build_response(query):
    transaction_id = get_transaction_id(query[:2])
    flags = get_flags(query[2:4])
    question_count = b"\x00\x01"
    answer_count = get_answer_count(query[12:])
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
