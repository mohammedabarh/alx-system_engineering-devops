#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """Prints sorted count of given keywords"""
    if word_count is None:
        word_count = {}
        for word in word_list:
            word_count[word.lower()] = 0

    if not subreddit or not isinstance(subreddit, str):
        return

    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=user_agent,
                              params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get('data', {})
        posts = data.get('children', [])
        after = data.get('after')

        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            for word in word_count:
                word_count[word] += title.split().count(word)

        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_counts = sorted(word_count.items(),
                                 key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")

    except Exception:
        return
