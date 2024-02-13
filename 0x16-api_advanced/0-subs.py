#!/usr/bin/python3
"""Script that returns the number of subscribers on Reddit
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    headers = {'User-Agent': user_agent}

    # check if valid subreddit
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
