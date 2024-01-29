#!/usr/bin/python3
"""A script the return user's todo list progress from
REST API dump the data to json file
"""
import json
import requests
import sys


if __name__ == '__main__':
    # the api endpoint structure
    base_url = 'https://jsonplaceholder.typicode.com'
    users_endpoint = f'/users'

    users = requests.get(base_url + users_endpoint).json()

    all_users_dict = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_todos = requests.get(base_url + users_endpoint
                                  + '/'
                                  + str(user_id)
                                  + '/todos')
        todos = user_todos.json()

        all_users_dict[user_id] = []

        for todo in todos:
            all_users_dict[user_id].append({
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            })
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as jsonfile:
        json.dump(all_users_dict, jsonfile)
