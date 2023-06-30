#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me and retrieve the response body
curl -s -X PUT -L -d "user_id=98" 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool"
