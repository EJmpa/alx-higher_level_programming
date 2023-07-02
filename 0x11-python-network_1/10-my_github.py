#!/usr/bin/python3
"""
Uses the GitHub API to display the user id using Basic Authentication.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        user_id = data.get("id")
        print(user_id)
    else:
        print("None")
