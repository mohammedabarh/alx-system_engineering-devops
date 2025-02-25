#!/usr/bin/python3
"""Module for querying the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot articles for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/your_username)'
    }
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
            hot_list.append(post.get('data', {}).get('title'))

        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list

    except Exception:
        return None
