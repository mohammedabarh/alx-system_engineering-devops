#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot articles for a given subreddit"""
    if not subreddit or not isinstance(subreddit, str):
        return None

    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=user_agent,
                              params=params, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get('data', {})
        posts = data.get('children', [])
        after = data.get('after')

        for post in posts:
            hot_list.append(post.get('data', {}).get('title'))

        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list

    except Exception:
        return None
