import socket

def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("127.0.0.1", 12345))
    print("UDP Server listening...")

    while True:
        msg, addr = server.recvfrom(1024)
        print(f"Client: {msg.decode()}")
        response = input("You: ")
        server.sendto(response.encode(), addr)
        if response == 'bye':
            print("Closing server.")
            break

udp_server()
