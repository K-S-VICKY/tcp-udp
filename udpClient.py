import socket

def udp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        msg = input("You: ")
        client.sendto(msg.encode(), ("127.0.0.1", 12345))
        if msg == 'bye':
            print("Closing client.")
            break
        response, _ = client.recvfrom(1024)
        print(f"Server: {response.decode()}")

    client.close()

udp_client()
