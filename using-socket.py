import socket
import sys

server_address = ('127.0.0.1', 43110)

# Create server socket and listen to 127.0.0.1 on port 43110
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

# Create a client socket and connect to the server socket on 127.0.0.1:43310
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

# Accept the connection from the client socket
connection, client_address = server_socket.accept()

# Send the "Hello, World!" message to the client from the server
connection.send(b"Hello, World!")

# Receive the "Hello, World!" message from the server and print it
hello = client_socket.recv(13).decode('utf-8')
print(hello)

# Close the sockets
client_socket.close()
server_socket.close()
