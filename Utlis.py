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

def format_sources_response(json_response):
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
    print("---| format_sources_response(json_response) preprocessing")
    
    # Load the JSON response into a dictionary
    json_response = json.loads(json_response["data"])
    
    # Extract information for the list of headlines
    list_details = []
    COUNT = 0  # Initialize a counter
    for source in json_response['sources']:
        # Create a dictionary to store details of each source
        source_details = {
            'source_name': source['name']  # Extract the source name
        }
        # Append the source details to the list
        list_details.append(source_details)

  # Check if the number of extracted sources has reached the READ_LIMIT
        if len(list_details) == READ_LIMIT:
            break  # If reached, exit the loop
        
    # Add the list of details to the formatted response dictionary
    formatted_response['list_details'] = list_details
    
    # Convert the formatted response dictionary to a JSON string
    json_string = json.dumps(formatted_response)
    
    # Return the JSON string
    return json_string


def format_sources_response_two(json_response):
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
    print("---| format_sources_response_two(json_response) preprocessing")
    
    # Extract parameters from the JSON response
    params = json_response["args"]
    
    # Load the JSON response into a dictionary
    json_response = json.loads(json_response["data"])
    
    # Extract information for the list of headlines
    list_details = []
    COUNT = 0  # Initialize a counter
    print("format_sources_response_two ", params)
    for source in json_response['sources']:
        # Check if the source name matches the specified source in the parameters
        if params["source"] == source['name']:
            # Create a dictionary to store details of the matching source

              source_details = {
                'source_name': source['name'],
                'country': source['country'],
                'description': source['description'],
                'URL': source['url'],
                'language': source['language'],
                'category': source['category']
            }
            # Append the source details to the list
            list_details.append(source_details)
        
        # Check if the number of extracted sources has reached the READ_LIMIT
        if len(list_details) == READ_LIMIT:
            break  # If reached, exit the loop
    
    # Add the list of details to the formatted response dictionary
    formatted_response['list_details'] = list_details
    
    # Convert the formatted response dictionary to a JSON string
    json_string = json.dumps(formatted_response)
    
    # Return the JSON string
    return json_string

def format_headlines_response_two(response):
    """
    Format the JSON response from the News API to match the required response type.
    
    Args:
    response (dict): The JSON response from the News API.
    
    Returns:
    dict: A dictionary containing the formatted response for both the list of headlines
          and the details of a selected headline.
    """
    print("---| format_headlines_response_two(response) preprocessing")
    
    # Convert data to JSON
    json_response = response["data"]
    json_response = json.loads(json_response)
    
    # Extract parameters from the response
    params = response["args"]
    
    # Initialize an empty dictionary to hold the formatted response
    formatted_response = {}
    
    # Extract information for the list of headlines
    list_details = []
    print(params)
    for article in json_response['articles']:
        #print(article)
        # Check if the article's source, author, and title match the specified parameters
        if article['source']['name'] == params['source'] and article['author'] == params['author'] and article['title'] == params['title']:
            # Extract and format the publish date and time
            published_at = article['publishedAt']
            published_at_datetime = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
            pub_date = published_at_datetime.date()
            pub_date_str = pub_date.isoformat()
            pub_time = published_at_datetime.time()
            
            # Create a dictionary to store details of the matching headline
            headline_details = {
                'source_name': article['source']['name'],
                'author': article['author'] if article['author'] else 'Unknown',
                'title': article['title'],
                'url': article['url'],
                'description': article['description'],
                'publish_date': pub_date_str,
                'publish_time': pub_time.strftime("%H:%M:%S")
            }




    
