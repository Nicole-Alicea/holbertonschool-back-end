#!/usr/bin/python3
'''This script returns information about
an employee's TODO list progress'''

import requests
import sys


def get_employee_todo_progress(employee_id):
    '''This method will retrieve the employee's progress and display it'''

    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    num_total_tasks = len(todos_data)
    num_done_tasks = sum(1 for task in todos_data if task['completed'])

    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_name = employee_response.json()["name"]

    print(f"Employee {employee_name} is done with tasks ({num_done_tasks}/{num_total_tasks}):")
    for task in todos_data:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)