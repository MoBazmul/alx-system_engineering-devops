#!/usr/bin/python3


import sys
import json
import requests

if __name__ == '__main__':
    # URL to the to dos API
    url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_details = {}
    todo_tasks = []
    
    # Concatenating the URL with specific user ID
    url = url + '?userId=' + sys.argv[1]
    user_url = user_url + '/' + sys.argv[1]
    
    obj = requests.get(url).json()
    
    # Getting the username
    username = requests.get(user_url).json()['name']
    
    json_file_name = sys.argv[1] + '.json'
    
    for o in obj:
        todo_tasks.append({"task": o['title'], "completed": o['completed'], "username": username})
    
    
    todo_details[str(sys.argv[1])] = todo_tasks
    
    with open(json_file_name, 'a') as file:
        json.dump(todo_details, file)

