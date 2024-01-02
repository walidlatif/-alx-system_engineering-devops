#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
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

    # Correct output formatting
    message = ''
    for task in todos:
        if task.get('userId') == int(user_id):
            message += 'Task {}: '.format(task.get('title'))
            message += str(task.get('completed'))
            message += '\n'

    # Correct user ID and username retrieved
    username = user.get('name')
    if username:
        message = 'User ID and Username: {}\n'.format(username) + message

    with open('{}.csv'.format(user_id), 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos:
            if task.get('userId') == int(user_id):
                writer.writerow([user_id, user.get('name'),
                                 task.get('completed'), task.get('title')])

    # Print the message
    print(message)
