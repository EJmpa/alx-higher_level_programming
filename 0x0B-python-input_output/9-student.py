#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """A class - Student."""

    def __init__(self, first_name, last_name, age):
        """Initializes the class `"Student"` attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the Student"""
        return self.__dict__
