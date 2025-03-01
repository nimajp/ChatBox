import socket
import threading

HOST = "0.0.0.0"  # Listen on all network interfaces
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server is waiting for a connection...")

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break  # Stop if the connection is closed
            print(f"Received: {message}")
            broadcast(message, client_socket)
        except:
            break
    client_socket.close()
    clients.remove(client_socket)

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode("utf-8"))
            except:
                client.close()
                clients.remove(client)

def accept_connections():
    while True:
        client_socket, addr = server.accept()
        print(f"Connected with {addr}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

accept_connections()
