#!/usr/bin/python3
"""A script the return user's todo list progress from
REST API
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

    total_todos = len(todo_response.json())
    completed_todos = [todo for todo in todo_response.json()
                       if todo.get('completed')]

    print('Employee {} is done with tasks({}/{}):'.format(
        user_response.json().get('name'),
        len(completed_todos),
        total_todos))

    for todo in completed_todos:
        print('\t {}'.format(todo.get('title')))
