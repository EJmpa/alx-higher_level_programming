#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass `"square"`"""

    def __init__(self, size):
        """Initialize a new class `"square"`
        """
        super().__init__(size, size)
        
        self.integer_validator("size", size)
        self.__size = size
