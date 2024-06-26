#!/usr/bin/python3
"""
A Script that, uses this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import sys
import requests

if __name__ == '__main__':
    # URL to the to dos API
    url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"
    
    # Concatenating the URL with specific user ID
    url = url + '?userId=' + sys.argv[1]
    user_url = user_url + '/' + sys.argv[1]
    
    obj = requests.get(url).json()
    
    # Getting the username
    username = requests.get(user_url).json()['name']
    
    no_of_tasks = len(obj)
    completed_tasks = []
    
    for o in obj:
        if o['completed'] == True:
            completed_tasks.append(o['title'])
            
    print(f"Employee {username} is done with tasks({len(completed_tasks)}/{no_of_tasks}):")
    
    for task in completed_tasks:
        print(f"\t{task}")




