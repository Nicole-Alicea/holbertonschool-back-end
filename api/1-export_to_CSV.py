#!/usr/bin/python3
'''This extends the script used in task 0 so that it exports data
in the CSV format'''

import csv
import requests
import sys


def export_employee_todo_to_csv(employee_id, employee_name, todos_data):
    filename = f'{employee_id}.csv'
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']
    
    with open(filename, 'w', newline='') as csvfile:
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos_data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': 'Completed' if task['completed']
                else 'Incomplete',
                'TASK_TITLE': task['title']
            })

    print(f"Data exported to {filename}")


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    employee_url = f"{base_url}/users/{employee_id}"

    # Fetching todos for the employee
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Fetching employee info
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    export_employee_todo_to_csv(employee_id, employee_name, todos_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
