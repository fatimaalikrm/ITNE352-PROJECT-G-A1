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
#6.Receive the client's username and print a connection message.
        client_username = client_socket.recv(1024).decode()
        print(f"[*] Client '{client_username}' connected.")

#7.Enter a loop to handle multiple client requests
        while True:
            # Receive the client's request
            request = client_socket.recv(1024).decode()

            if request.lower() == 'quit':
                print(f"[*] {client_username} disconnected.")
                break

#8. Receive the client's request and process it
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

    def getSpec(request):
    #{"version": 2,"choice":BBC News_https://www.facebook.com/bbcnews_Children used as 'guinea pigs' in clinical trials,"param",1.1_bbc
    print(request)
    data = request["choice"]
    details = {"source":data[0],"author":data[1],"title":data[2]}
    request = {"version": 1,"choice":request['param']}
    request  = json.dumps(request)
    print(request)
    response = process_request(request)
    response["version"] = 2
    response["args"] = details
    return response

def getSpec_s4(request):
    #{"version": 2,"choice":BBC News_https://www.facebook.com/bbcnews_Children used as 'guinea pigs' in clinical trials,"param",1.1_bbc
    print("S4 ",request)
    data = request["choice"]
    details = {"source":data[0]}
    request = {"version": "s1","choice":request['param']}
    request  = json.dumps(request)
    print(request)
    response = process_request(request)
    response["version"] = "s5"
    response["args"] = details
    return response


# Function to process client requests
def process_request(request, client_username="temp"):
    # Split the request into parts
    request = json.loads(request)
    
    # Check the version of the request
    if request["version"] == 2:
        return getSpec(request)
    
    # Process based on different versions or types of requests
    if request["version"] == "s4":
        return getSpec_s4(request)
    
    if request["version"] == "s1":
        return process_sources_request(request, client_username)
    
    # Split the choice to determine the category
    parts = request["choice"].split("_")
    category = parts[0]
    data = "not"
    
    # Print the received category for debugging purposes
    print("---Received --- " + category)
    
    # Process the request based on the category
    if category == '1.1':  # Search for keywords
        keyword = parts[1]
        data = search_by_keyword(keyword)
    elif category == '1.2':  # Search by category
        category = parts[1]
        data = search_by_category(category)
    elif category == '1.3':  # Search by country
        country = parts[1]
        data = search_by_country(country)
    elif category == '1.4':  # List all headlines
        data = list_all_headlines()
    else:
        return "Invalid category"

#10. Save the data to a JSON file.
    if client_username != "temp":
        filename = f"{GROUP_ID}_{client_username}_{parts[1]}_sources.json"
        save_to_json(data, filename)
    return {"data":data,"version": "s3"}





