#!/usr/bin/python3

#Importation of `Base` class from `'models/base.py'
from models.base import Base

class Rectangle(Base):
    """class `'Rectangle'` that inherits
    'Base' class features
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """`Rectangle` class initialzation"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    
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
        if (type(value) is not int):
            raise TypeError(f"width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value


    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if (type(value) is not int):
            raise TypeError(f"height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value
        
    @x.setter
    def x(self, value):
        """Sets the value of x"""
        if (type(value) is not int):
            raise TypeError(f"x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value
        
    @y.setter
    def y(self, value):
        """Sets the value of y"""
        if (type(value) is not int):
            raise TypeError(f"y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
        
    def area(self):
        """Returns the area value of the `'Rectangle'` instance"""
        return (self.__width * self.__height)
    
    def display(self):
        """A function that prints in stdout the `'Rectangle'`
        instance with the character '#'
        """
        for y in range(self.y):
            print("")
        for h in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.__width):
                print ("#", end="")
            print()
            
    def __str__(self):
        """Returns '[Rectangle] (<id>) <x>/<y> - <width>/<height>'"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"
    
    def update(self, *args, **kwargs):
        """A method that updates attributes by assigning
        an argument to each of them
        """
        if args and len(args) != 0:
            i = 0
            for arg in ls:
                if i == 0:
                    if len(ls) == 0:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
            
        elif (kwargs) and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
