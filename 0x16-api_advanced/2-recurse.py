#!/usr/bin/python3
"""Script that returns the number of subscribers on Reddit
"""
import requests


after = None


def recurse(subreddit, hot_list=None):
    """Returns the number of subscribers
    """
    if hot_list is None:
        hot_list = []

    global after
    user_agent = {'User-Agent':
                  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': after}
    results = requests.get(url, params=parameters,
                           headers=user_agent, allow_redirects=False)

    if results.status_code == 200:
        data = results.json().get("data")
        after_data = data.get("after")
        if after_data:
            after = after_data
            recurse(subreddit, hot_list)

        all_titles = data.get("children")
        for post in all_titles:
            hot_list.append(post.get("data").get("title"))

        return hot_list
    else:
        return None
