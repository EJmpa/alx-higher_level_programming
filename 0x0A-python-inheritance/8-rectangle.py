#!/usr/bin/python3
"""Inherits `BaseGeometry` from `"baseGeometry"` module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class to define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize class Rectangle parameters
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
