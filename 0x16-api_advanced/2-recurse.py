#!/usr/bin/python3
"""
Module for recursively querying the Reddit API to get hot posts
"""
import requests

# Global variable for pagination
after = None


def recurse(subreddit, hot_list=[]):
    """
    Returns a list of titles of all hot posts for a given subreddit recursively.

    Args:
        subreddit (str): The subreddit to query
        hot_list (list): List to store the titles (default empty list)

    Returns:
        list: List of all hot post titles if successful
        None: If subreddit is invalid
    """
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    
    try:
        results = requests.get(url, 
                             params=parameters, 
                             headers=user_agent,
                             allow_redirects=False)

        if results.status_code == 200:
            data = results.json().get("data", {})
            after_data = data.get("after")
            
            # Get all posts from current page
            all_titles = data.get("children", [])
            for title_ in all_titles:
                hot_list.append(title_.get("data", {}).get("title"))

            # If there's a next page, recurse
            if after_data is not None:
                after = after_data
                recurse(subreddit, hot_list)
            
            return hot_list
        else:
            return None

    except Exception:
        return None
