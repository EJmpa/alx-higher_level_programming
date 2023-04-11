#!/usr/bin/python3
"""
    A Module that will return the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """A functions that looks out for all attributes and methods of an object"""
    return dir(obj)
