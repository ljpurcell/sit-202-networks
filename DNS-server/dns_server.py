from socket import socket, AF_INET, SOCK_DGRAM

HOST = "127.0.0.1"
PORT = 8080

a_records = {
    "localhost": "127.0.0.1", 
    "google.com": "172.253.122.100",
    "github.com": "192.30.255.113",
    "microsoft.com": "20.112.250.133",
    "wikipedia.com": "208.80.154.232",
    "twitter.com": "104.244.42.1",
}

cname_records = {
    "www.github.com" : "github.com",
    "www.instagram.com": "geo-p42.instagram.com",
    "www.stanford.edu": "pantheon-systems.map.fastly.net",
    "www.stripe.com": "stripe.com"
}


with socket(AF_INET, SOCK_DGRAM) as s:
    s.bind((HOST, PORT)) 
    print(f"Server running on {HOST}:{PORT}...")

    while True:
        domain = ""
        lookup_type = "both"
        response = ""
        query, addr = s.recvfrom(1024)
        if not query:
            break
        msg = query.decode().lower().strip()
        if " " in msg:
            domain = msg.split(" ")[0]
        else:
            domain = msg

        if "--only=" in msg:
            only_argument = msg.split("--only=")[1]
            if only_argument in ["both", "cname", "a"]:
                lookup_type = only_argument

        if lookup_type == "cname":
            response = f"CNAME record: {str(cname_records.get(domain))}"
        elif lookup_type == "a":
            response = f"A record: {str(a_records.get(domain))}"
        elif lookup_type == "both":
            response = f"CNAME record:  {str(cname_records.get(domain))}. A record: {a_records.get(domain)}"
        else:
            response = "Error: Sorry, we can't seem to generate a proper response right now."

        s.sendto(response.encode('utf-8'), addr)
