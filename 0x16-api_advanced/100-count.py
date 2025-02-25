#!/usr/bin/python3
"""
Module to recursively query the Reddit API and count keyword occurrences in hot post titles.
"""

import requests

def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): The 'after' parameter for pagination (default is None).
        word_count (dict): A dictionary to store the word counts (default is None).

    Returns:
        None
    """
    # Initialize word_count if it's the first call
    if word_count is None:
        word_count = {}

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
            
            # Process each post title
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    # Check if the word is in the title (case-insensitive)
                    if f' {word.lower()} ' in f' {title} ':
                        # Increment the word count
                        word_count[word.lower()] = word_count.get(word.lower(), 0) + 1
            
            # Get the 'after' parameter for the next page
            after = data['data']['after']
            
            # If there's a next page, make a recursive call
            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                # If there are no more pages, print the results
                if word_count:
                    # Sort the word_count dictionary
                    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                    # Print the results
                    for word, count in sorted_words:
                        print(f"{word}: {count}")
                return None
        else:
            # If the status code is not 200, return None
            return None
    except requests.RequestException:
        # If there's an error with the request, return None
        return None
