import socket

def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 1212))
    server.listen(1)
    print("Server is listening")

    client, addr = server.accept()
    print(f"Connection from {addr}")
    while True:
        msg = client.recv(1024).decode()
        if msg == "bye":
            print(f"Closing Connection...")
            break

        print(f"Client : {msg}")
        response = input("You: ")
        client.send(response.encode())

    client.close()
tcp_server()
