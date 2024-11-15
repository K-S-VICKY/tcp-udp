import socket

def tcp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 1212))
    
    while True:
        msg = input("You: ")
        client.send(msg.encode())
        if msg  == "bye":
            print("Closing conxn...")
            break
        response = client.recv(1024).decode()
        print(f"Server: {response}")
    client.close()

tcp_client()
        