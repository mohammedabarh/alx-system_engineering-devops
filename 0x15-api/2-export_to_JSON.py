#!/usr/bin/python3
"""Script that exports TODO list information to JSON format"""

import json
import requests
import sys


def export_to_json(employee_id):
    """Export TODO list information to JSON format"""
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    try:
        user = requests.get(user_url).json()
        todos = requests.get(todos_url).json()

        tasks = []
        for todo in todos:
            tasks.append({
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": user.get('username')
            })

        json_data = {str(employee_id): tasks}
        filename = "{}.json".format(employee_id)

        with open(filename, 'w') as json_file:
            json.dump(json_data, json_file)

    except Exception as e:
        print("Error occurred: {}".format(e))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
