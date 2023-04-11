#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """this class represents a base geometry"""

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class to define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize class Rectangle parameters
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        
    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns the print() and str() representation of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
