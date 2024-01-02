#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: ', sys.argv[0], '<employee id>')
        sys.exit(1)

    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url + '/users/{}'.format(user_id)).json()
    todos = requests.get(url + '/users/{}/todos'.format(user_id)).json()

    completed_tasks = [task for task in todos if task.get('completed') is True]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
          len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
