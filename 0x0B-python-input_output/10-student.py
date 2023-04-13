#!/usr/bin/python3

class Student:
    """Defines a student by first name, last name, and age."""
    def __init__(self, first_name, last_name, age):
        """Instantiates a Student object with the given attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
