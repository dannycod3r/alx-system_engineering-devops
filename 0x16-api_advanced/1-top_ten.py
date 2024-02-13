#!/usr/bin/python3
"""Script that returns the number of subscribers on Reddit
"""
import requests


def top_ten(subreddit):
    """Returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    headers = {'User-Agent': user_agent}

    # check if valid subreddit
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data').get('children')

        if len(posts) == 0:
            print("No posts found.")
            return

        for post in posts:
            print(post.get('data').get('title'))
    else:
        print("None")
