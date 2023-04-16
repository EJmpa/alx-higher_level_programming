#!/usr/bin/python3

#Importation of `Base` class from `'models/base.py'
from models.base import Base

class Rectangle(Base):
    """class `'Rectangle'` that inherits
    'Base' class features
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """`Rectangle` class initialzation"""
        super().__init__()
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        
    
    #Assign easch private instance attributes with its own public getter and setter:
    
    @property
    def width(self):
        """Gets/Returns the value of width"""
        return self.__width
    
    @property
    def height(self):
        """Gets/Returns the value of height"""
        return self.__height
    
    @property
    def x(self):
        """Gets/Returns the value of x"""
        return self.__x
    
    @property
    def y(self):
        """Gets/Returns the value of y"""
        return self.__y
    
    @width.setter
    def width(self, value):
        """Sets the value of width"""
        self.__width = value


    @height.setter
    def height(self, value):
        """Sets the value of height"""
        self.__height = value
        
    @x.setter
    def x(self, value):
        """Sets the value of x"""
        self.__x = value
        
    @y.setter
    def x(self, value):
        """Sets the value of y"""
        self.__y = value
        
        
