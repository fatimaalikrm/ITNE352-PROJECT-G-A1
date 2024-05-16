#1. import the necessary modules
import socket
import threading
import json
import requests
import signal
import sys
from utils import *

#2. Set configuration parameters
YOUR_API_KEY = 'e8a67a4811dc44abbcf6d5f38d1b330b'
GROUP_ID = "7566"
LANG = 'en'
# Define the server's IP address and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5050

#3. Create a TCP socket object and bind it to the server host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

#4. Start listening for incoming connections
server_socket.listen(3) 
print(f"[*] Server listening on {SERVER_HOST}:{SERVER_PORT}")

#5. Define a function to handle each client connection.
# Inside the handle_client function
def handle_client(client_socket, client_address):
    print(f"[*] Accepted connection from {client_address}")

    try:
        # Receive the client's username
        client_username = client_socket.recv(1024).decode()
        print(f"[*] Client '{client_username}' connected.")

        # Main loop to handle client requests
        while True:
            # Receive the client's request
            request = client_socket.recv(1024).decode()

            if request.lower() == 'quit':
                print(f"[*] {client_username} disconnected.")
                break

            # Process the request and send response
            print("Client Request Request --- "+request.lower())
            response = process_request(request,client_username)

            # Format the response
            if response["version"] == 1:
                response = format_headlines_response(response["data"])

            elif response["version"] == 2:
                 response = format_headlines_response_two(response)

            elif response["version"] == "s3":
                 response = format_sources_response(response)

            elif response["version"] == "s5":
                 response = format_sources_response_two(response)

            
            client_socket.send(response.encode())

    except socket.timeout:
        print("Timeout: No response to client within 1 minute.")
        client_socket.send("Server timeout: No response within 1 minute.".encode())
    except Exception as e:
        print(f"Error: {e}")

    # Close the client connection
    client_socket.close()

6.



