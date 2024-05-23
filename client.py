#1.Imports and Initializations
#imports the `socket` and `json` modules
import socket
import json

#defines the server's IP address and port
SERVER_HOST = '127.0.0.1'  # Change this to the server's IP address
SERVER_PORT = 5050

#creates a TCP socket and sets a timeout for socket operations (1 minute).
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(60)

#connects the client to the server.
client_socket.connect((SERVER_HOST, SERVER_PORT))

#prompts the user to enter a username and sends it to the server.
username = input("Enter your username: ")
client_socket.send(username.encode())

