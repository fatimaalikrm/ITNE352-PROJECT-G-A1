import json
from datetime import datetime

READ_LIMIT = 15

def save_to_json(data, filename):
    """
    Save data to a JSON file.
    Args:
    data (dict): The data to be saved.
    filename (str): The name of the JSON file.
    """
    with open(filename, 'w') as f:
        f.write(data)



def format_headlines_response(json_response):
    """
    Format the JSON response from the News API to match the required response type.
    
    Args:
    json_response (dict): The JSON response from the News API.
    
    Returns:
    dict: A dictionary containing the formatted response for both the list of headlines
          and the details of a selected headline.
    """
    # Initialize an empty dictionary to hold the formatted response
    formatted_response = {}
    
    # Print a preprocessing message
    print("---| format_headlines_response(json_response) preprocessing")
    
    # Load the JSON response into a dictionary
    json_response = json.loads(json_response)


    
