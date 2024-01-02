#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
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

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        })

    with open('{}.json'.format(user_id), 'w') as file:
        json.dump({user_id: tasks}, file)
