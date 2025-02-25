#!/usr/bin/python3
"""
Module for function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Queries Reddit API and counts keywords in hot post titles
    Args:
        subreddit: subreddit name
        word_list: list of keywords to count
        after: token for next page
        count_dict: dictionary to store word counts
    """
    # Initialize count_dict on first call
    if count_dict is None:
        count_dict = {}
        for word in word_list:
            # Convert to lowercase and remove duplicates
            word = word.lower()
            if word not in count_dict:
                count_dict[word] = 0

    # Set custom User-Agent to avoid too many requests error
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'
    }

    # Set URL and parameters for API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}

    try:
        # Make GET request to Reddit API
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        # Return if subreddit is invalid
        if response.status_code != 200:
            return

        # Parse response data
        data = response.json().get('data', {})
        posts = data.get('children', [])
        after = data.get('after')

        # Count keywords in post titles
        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            words = title.split()
            for word in count_dict:
                count_dict[word] += words.count(word)

        # Recursively get next page if it exists
        if after:
            return count_words(subreddit, word_list, after, count_dict)
        else:
            # Sort and print results
            sorted_counts = sorted(
                count_dict.items(),
                key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")

    except Exception:
        return
