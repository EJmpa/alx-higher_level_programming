#!/bin/bash
# Sends a GET request to a URL and displays the body of the response
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [[ $response -eq 200 ]]; then
    curl -s "$1"
fi

