import socket

# Create socket for server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Use your public IP and the port number you set in port forwarding
server.bind(('0.0.0.0', 12345))  # Use '0.0.0.0' to accept connections from any IP
server.listen(1)  # Allow server to listen for 1 connection

print("Server is waiting for a connection...")
client_socket, client_address = server.accept()  # Accept connection from client
print(f"Connection established with {client_address}")

# Keep the communication open until 'exit' is typed
while True:
    # Receive message from client
    message = client_socket.recv(1024).decode()
    if message.lower() == 'exit':  # Exit condition
        print("Client disconnected.")
        break

    print(f"Client: {message}")

    # Get response from the server and send it back to client
    response = input("You (Server): ")  # Server's input (chat response)
    client_socket.send(response.encode())  # Send server's response to client

client_socket.close()  # Close the connection after chatting