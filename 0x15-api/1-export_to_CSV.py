#!/usr/bin/python3
"""
Script that exports TODO list data for an employee to CSV format
"""
import csv
import requests
import sys


def export_todo_to_csv(employee_id):
    """Export TODO list data to CSV for given employee ID"""
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

    # Write to CSV
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                employee_id,
                user.get('username'),
                todo.get('completed'),
                todo.get('title')
            ])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_todo_to_csv(int(sys.argv[1]))
