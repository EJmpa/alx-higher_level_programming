#!/usr/bin/python3
"""A module that defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """This function returns the JSON representation of a string object"""
    return json.dumps(my_obj)
