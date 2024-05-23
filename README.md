# News Headlines and Sources Retrieval System

# Project Description
This project is a client-server system for retrieving news
headlines and sources using the News API. The system allows users to 
interact with the server to search for headlines by keyword, category,
or country, as well as to list all headlines. Additionally, users can
search for news sources by category, country, or language, or list all 
available sources.

# Semester 
Second Semseter 2023-2024

# Group 
**Group Name:** [A1 - Creative]  
**Course Code:** [ITNE352]  
**Section:** [1]  
**Student Name:** [Fatima Ali,Alzahraa Hussain]  
**Student ID:** [202108358, 202101299]

## Table of Contents
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Scripts](#scripts)
- [Additional Concept](#additional-concept)
- [Acknowledgments](#acknowledgments)
- [Conclusion](#conclusion)
- [Resources](#resources) (optional)

# Requirements

The project requires the following:
- `socket`: This module provides access to the BSD socket interface. 
- `threading`: This module provides classes and functions for multi-threaded programming. 
- `json`: This module provides functions for encoding and decoding JSON data. 
- `requests`: This module allows sending HTTP requests easily. 
- `signal`: This module provides mechanisms to handle signals received by the program.
- `utils`: This is a custom module containing utility functions used in the project.

# How to Run
To run the system:
1. Obtain a News API key from [News API website](https://newsapi.org/) and replace `'YOUR_API_KEY'` in `server.py` and `client.py` with your actual API key.
2. Start the server by running `server.py`.
3. Run `client.py` to interact with the server.
4. Follow the instructions provided by the client to search for headlines or sources.

   
# Scripts
## 1.client.py
`client.py` is the client-side script responsible for interacting with the server.
 It prompts users for input, sends requests to the server, and displays the retrieved data to the user.
 The script utilizes the `socket` and `json` modules for communication with the server.

## 2.server.py
`server.py` is the server-side script responsible for handling client requests and communicating with the News API. 
It listens for incoming connections, processes client requests, retrieves data from the News API, and sends responses back to the client. The script utilizes the `socket`, `threading`, `json`, `requests`, `signal`, and custom utility functions from `utils.py`.

# Additional Concept
The project utilizes multi-threading to handle multiple client connections concurrently. This allows the server to handle multiple requests simultaneously without blocking.


# Acknowledgments
Our indebtedness to News API as indispensable when it comes to how efficiently they have instructed us their API could be fully employed. The expansive guidebooks and tutorials they have put together would be said to form a basis for the origin of this project. It would be a lie not to acknowledge that deploying functionalities integrated in this system would have been a slightly harder task were it not for their clear and precise documentation







