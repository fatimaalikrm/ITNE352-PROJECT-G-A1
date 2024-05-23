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

# Extract information for the list of headlines
    list_details = []
    COUNT = 0  # Initialize a counter
    for article in json_response['articles']:
        # Create a dictionary to store details of each headline
        headline_details = {
            'source_name': article['source']['name'],
            'author': article['author'] if article['author'] else 'Unknown',
            'title': article['title']
        }
        # Append the headline details to the list
        list_details.append(headline_details)
        
        # Check if the number of extracted headlines has reached the READ_LIMIT
        if len(list_details) == READ_LIMIT:
            break  # If reached, exit the loop

  # Add the list of details to the formatted response dictionary
    formatted_response['list_details'] = list_details
    
    # Convert the formatted response dictionary to a JSON string
    json_string = json.dumps(formatted_response)
    
    # Return the JSON string
    return json_string




    
