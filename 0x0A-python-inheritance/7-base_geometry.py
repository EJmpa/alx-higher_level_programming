#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """This class represents a base geometry"""

    def area(self):
        """method yet to be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
