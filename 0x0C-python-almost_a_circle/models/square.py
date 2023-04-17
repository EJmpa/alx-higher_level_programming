#!/usr/bin/python3

"""A Module that of a class `'Sqaure'` that inherits `'Rectangle'` class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """A 'Square'` class that inherits the '`Rectangle'` class"""
    def __init__(self, size, x=0, y=0, id=None):
        """`'Square'` class initialization"""
        self.id = id
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)
        
    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - \
{self.size}"
    
    @property
    def size(self):
        """Gets the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value
