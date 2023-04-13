#!/usr/bin/python3
"""This module defines a text file-reading function"""


def read_file(filename=""):
    """This funtion prints the contents of a UTF8 text file"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
