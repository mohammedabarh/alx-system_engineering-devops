# 0x16. API Advanced

This project contains Python scripts that interact with the Reddit API to fetch and process data about subreddits and their posts.

## Project Description

The goal of this project is to practice working with APIs, specifically the Reddit API. The tasks involve querying the API to retrieve information about subreddits, their subscribers, and posts. The project covers topics such as:

- Reading API documentation
- Using pagination with APIs
- Parsing JSON results
- Making recursive API calls
- Sorting dictionaries by value

## Files

### Mandatory Tasks

1. **0-subs.py**
   - Function: `number_of_subscribers(subreddit)`
   - Description: Queries the Reddit API and returns the number of subscribers for a given subreddit.

2. **1-top_ten.py**
   - Function: `top_ten(subreddit)`
   - Description: Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

3. **2-recurse.py**
   - Function: `recurse(subreddit, hot_list=[])`
   - Description: Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

### Advanced Task

4. **100-count.py**
   - Function: `count_words(subreddit, word_list)`
   - Description: Recursively queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

## Requirements

- Python 3.4.3 or higher
- Ubuntu 20.04 LTS
- `requests` library for making HTTP requests

## Usage

To use these scripts, you'll need to have Python 3 installed and the `requests` library. You can run the main files provided with each script to test the functions.

Example usage for `0-subs.py`:

```bash
python3 0-main.py programming
