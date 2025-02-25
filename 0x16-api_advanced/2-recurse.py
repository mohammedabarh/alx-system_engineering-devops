#!/usr/bin/python3
"""
Module to recursively query the Reddit API for all hot posts in a subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store the post titles (default is an empty list).
        after (str): The 'after' parameter for pagination (default is None).

    Returns:
        list: A list containing the titles of all hot articles, or None if the subreddit is invalid.
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'ALX API Advanced Project'}
    
    # Construct the API URL
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    if after:
        url += f'&after={after}'
    
    try:
        # Send a GET request to the API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Get the list of posts
            posts = data['data']['children']
            
            # Add the titles to the hot_list
            for post in posts:
                hot_list.append(post['data']['title'])
            
            # Get the 'after' parameter for the next page
            after = data['data']['after']
            
            # If there's a next page, make a recursive call
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                # If there are no more pages, return the complete list
                return hot_list
        else:
            # If the status code is not 200, return None
            return None
    except requests.RequestException:
        # If there's an error with the request, return None
        return None
