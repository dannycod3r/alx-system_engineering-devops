#!/usr/bin/python3
"""A script the return user's todo list progress from
REST API and export to csv file
"""
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

    todos = todo_response.json()
    username = user_response.json().get('username')

    filename = userId + '.csv'
    with open(filename, mode='w') as csvfile:
        for todo in todos:
            csvfile.write('"{}","{}","{}","{}"\n'
                          .format(userId,
                                  username,
                                  todo.get('completed'),
                                  todo.get('title')))
