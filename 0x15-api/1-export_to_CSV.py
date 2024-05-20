#!/usr/bin/python3
"""
A Script that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
exporting data in the CSV format.
"""

import sys
import csv
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
    
    csv_file_name = sys.argv[1] + '.csv'
    
    with open(csv_file_name, 'a') as file:
        writer = csv.writer(file)
        
        for o in obj:
            writer.writerow([str(sys.argv[1]), username, o['completed'], o['title']])




