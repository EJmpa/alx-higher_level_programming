#!/bin/bash
# Send a GET request to a URL with a header variable and display the body of the response
curl -sH "X-School-User-Id: 98" "$1"
