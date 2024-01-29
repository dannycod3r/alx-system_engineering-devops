#!/usr/bin/python3
"""A script the return user's todo list progress from
REST API
"""
import json
import requests
import sys


if __name__ == '__main__':
    # the api endpoint structure
    base_url = 'https://jsonplaceholder.typicode.com'
    userId = sys.argv[1]  # get the userId as argument
    user_endpoint = f'/users/{userId}'
    todos_endpoint = f'/user/{userId}/todos'

    user_response = requests.get(base_url + user_endpoint)
    todo_response = requests.get(base_url + todos_endpoint)

    username = user_response.json().get('username')
    user_todos_dict = {userId: []}

    for todo in todo_response.json():
        user_todos_dict[userId].append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        })
    filename = userId + '.json'
    with open(filename, 'w') as jsonfile:
        json.dump(user_todos_dict, jsonfile)
