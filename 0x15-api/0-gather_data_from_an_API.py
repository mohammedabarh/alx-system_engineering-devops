#!/usr/bin/python3
"""
Script that uses REST API to get TODO list progress for a given employee ID
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Get TODO list progress for given employee ID"""
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee info
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        return
    user = user_response.json()

    # Get TODO list
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        return
    todos = todos_response.json()

    # Calculate progress
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo.get('completed')])

    # Display progress
    print(f"Employee {user.get('name')} is done with tasks"
          f"({done_tasks}/{total_tasks}):")

    # Display completed tasks
    for todo in todos:
        if todo.get('completed'):
            print(f"\t {todo.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_employee_todo_progress(int(sys.argv[1]))
