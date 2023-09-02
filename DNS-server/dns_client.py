from socket import socket, AF_INET, SOCK_DGRAM

HOST = "127.0.0.1" 
PORT = 8080  
QUIT_COMMAND = ":q!"

with socket(AF_INET, SOCK_DGRAM) as s:
    s.connect((HOST, PORT))  

    print("\n\tWelcome to this DNS service\n")
    print(
        "Please type in the domain you wish to query. The server will return both A and CNAME record information unless you specify only one."
    )
    print("EXAMPLE: 'www.google.com --only=A'--> returns only A record information.")
    print("EXAMPLE: 'www.google.com --only=CNAME'--> returns only CNAME record information.")
    print(f"(Or type '{QUIT_COMMAND}' to quit)")

    while True:
        query = input("\nDomain: ").strip()
        if query == QUIT_COMMAND:
            break

        s.send(query.encode('utf-8'))

        response = s.recv(1024).decode()
        print(response)

        user_input = input(f"Type '{QUIT_COMMAND}' to quit or press ENTER to continue.").strip()
        if user_input == QUIT_COMMAND:
            break

    print("Goodbye!")
