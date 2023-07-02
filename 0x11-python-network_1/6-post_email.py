#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter
and displays the body of the response
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    print("Your email is:", response.text)
