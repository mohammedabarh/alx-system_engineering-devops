#!/usr/bin/python3
"""
Module to query the Reddit API for the top 10 hot posts in a subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'ALX API Advanced Project'}
    
    # Construct the API URL
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    
    try:
        # Send a GET request to the API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Get the list of posts
            posts = data['data']['children']
            # Print the titles of the first 10 posts
            for post in posts:
                print(post['data']['title'])
        else:
            # If the status code is not 200, print None
            print(None)
    except requests.RequestException:
        # If there's an error with the request, print None
        print(None)
