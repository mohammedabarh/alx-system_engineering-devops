#!/usr/bin/python3
"""Script that exports all TODO list information to JSON format"""

import json
import requests


def export_all_to_json():
    """Export all TODO list information to JSON format"""
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{}/users".format(base_url)

    try:
        users = requests.get(users_url).json()
        all_tasks = {}

        for user in users:
            user_id = str(user.get('id'))
            username = user.get('username')
            todos_url = "{}/todos?userId={}".format(base_url, user_id)
            todos = requests.get(todos_url).json()

            user_tasks = []
            for todo in todos:
                user_tasks.append({
                    "username": username,
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                })

            all_tasks[user_id] = user_tasks

        with open('todo_all_employees.json', 'w') as json_file:
            json.dump(all_tasks, json_file)

    except Exception as e:
        print("Error occurred: {}".format(e))


if __name__ == "__main__":
    export_all_to_json()
