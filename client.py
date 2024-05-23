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

#2.Main Menu and Navigation:
#defines three main functions: `display_main_menu()`, `display_headlines_menu()`, and `display_sources_menu()`.
#The `display_main_menu()` function presents the user with three options: search headlines, list of sources, and quit.
def display_main_menu():
    print("Main Menu:")
    print("1. Search headlines")
    print("2. List of Sources")
    print("3. Quit")

#The `display_headlines_menu()` and `display_sources_menu()` functions provide various search and display options for headlines and sources, respectively.
# Function to display the headlines menu
def display_headlines_menu():
    print("Headlines Menu:")
    print("1. Search by keyword")
    print("2. Search by category")
    print("3. Search by country")
    print("4. List all headlines")
    print("5. Back to main menu")

#The user's choices are processed, and the appropriate requests are sent to the server.
 user_choice = input(">>>")
    word_search = ""
    if user_choice == '1':
        word_search = get_input("Keyword")
    elif user_choice == '2':
        print("-- Categories --")
        print("business, entertainment, general, health, science, sports, technology")
        word_search = get_input("Category")
    elif user_choice == '3':
        print("--Countiries--")
        print("au, nz, ca, ae, sa, gb, us, eg, ma")
        word_search = get_input("Country")

    elif user_choice == '4':
        word_search = "all"
    elif user_choice == '5':
        word_search = "return"
    else:
        print("Invalid choice!!")
        display_headlines_menu()

    return ["1." + user_choice + "_" + word_search, word_search]

# Function to display the sources menu
def display_sources_menu():
    print("Sources Menu:")
    print("1. Search by category")
    print("2. Search by country")
    print("3. Search by language")
    print("4. List all")
    print("5. Back to main menu")
  
  #The user's choices are processed, and the appropriate requests are sent to the server.
  user_choice = input(">>>")
    word_search = ""
    if user_choice == '1':
        print("-- Categories --")
        print("business, entertainment, general, health, science, sports, technology")
        word_search = get_input("Category")
    elif user_choice == '2':
        print("--Countiries--")
        print("au, nz, ca, ae, sa, gb, us, eg, ma")
        word_search = get_input("Country")
    elif user_choice == '3':
        print("-- Language --")
        print("ar, en")
        word_search = get_input("Language")
    elif user_choice == '4':
        word_search = "all"
    elif user_choice == '5':
        word_search = "return"
    else:
        print("Invalid choice!!")
        display_sources_menu()

    return ["2." + user_choice + "_" + word_search, word_search]

#3.Displaying Results:
#The `display_list_details()` function takes a list of details (either headlines or sources) and prints them in a formatted way.
def display_list_details(list_details):
    """
    Display each item in the list of details.
    Args:
    list_details (list): A list of dictionaries containing details.
    """
    list_data = []
    count = 1
    for item in list_details:
        print("#" + str(count), end="|")
        print("Source Name:", item.get("source_name"), end=" ")
        print("Author:", item.get("author"), end=" ")
        print("Title:", item.get("title"), end="\n")
        print("-" * 50)  # Separating each item
        count += 1
        list_data.append([item.get("source_name"), item.get("author"), item.get("title")])

    return list_data

def get_input(msg):
    print("---- Search By " + msg)
    search_word = input("-->")
    return search_word

#The `print_list_details_headlines()` and `print_list_details_sources()` functions are used to display the details of individual headlines or sources, respectively.
def print_list_details_headlines(details):
    # print(details)
    """
    Print the details of each item in the list of details.
    Args:
    details (dict): A dictionary containing a list of details.
    Returns:
    None
    """
    # Iterate over the list of details
    for item in details["list_details"]:
        # Print each detail of the item
        print("Source Name:", item["source_name"])
        print("Author:", item["author"] if item["author"] else "None")
        print("Title:", item["title"])
        print("URL:", item["url"])
        print("Description:", item["description"])
        print("Publish Date:", item["publish_date"])
        print("Publish Time:", item["publish_time"])


def print_list_details_sources(details):
    # print(details)
    """
    Print the details of each item in the list of details.
    Args:
    details (dict): A dictionary containing a list of details.
    Returns:
    None
    """
    # Iterate over the list of details
    for item in details["list_details"]:
        # Print each detail of the item
        print("Source Name:", item["source_name"])
        print("country:", item["country"])
        print("Category:", item["category"])
        print("URL:", item["URL"])
        print("Description:", item["description"])
        print("Language:", item["language"])




