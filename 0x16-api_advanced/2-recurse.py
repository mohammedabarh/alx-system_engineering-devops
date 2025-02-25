#!/usr/bin/python3
"""
Module for querying the Reddit API recursively to get hot posts
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Returns a list containing the titles of all hot articles for a given subreddit
    Args:
        subreddit: The subreddit to search
        hot_list: List to store titles (default None)
        after: Token for pagination (default None)
    Returns:
        List of titles if successful, None if subreddit is invalid
    """
    if hot_list is None:
        hot_list = []

    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/your_username)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers,
                              params=params, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get('data', {})
        posts = data.get('children', [])
        after = data.get('after')

        for post in posts:
            title = post.get('data', {}).get('title')
            hot_list.append(title)

        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list

    except Exception:
        return None
