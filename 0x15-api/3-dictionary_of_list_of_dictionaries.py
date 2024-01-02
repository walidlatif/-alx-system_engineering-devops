#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get('{}/users'.format(url)).json()

    all_tasks = {}
    for user in users:
        user_id = user.get('id')
        todos = requests.get('{}/users/{}/todos'.format(url, user_id)).json()

        tasks = []
        for task in todos:
            tasks.append({
                "username": user.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
            })

        all_tasks[user_id] = tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file)
