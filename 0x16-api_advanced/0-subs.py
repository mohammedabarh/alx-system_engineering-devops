#!/usr/bin/python3
"""
Module to query the Reddit API for the number of subscribers in a subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'ALX API Advanced Project'}
    
    # Construct the API URL
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        # Send a GET request to the API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the status code is not 200, return 0
            return 0
    except requests.RequestException:
        # If there's an error with the request, return 0
        return 0
