#!/usr/bin/python3

"""This module stores a class named `'Base'`"""

class Base:
    """A Python class - 'Base' for evaluation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """An dunder method(__init__()) for
        initializing `'Base'` class arguments
        """

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

            
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
        for h in range(self.__height):
            for w in range(self.__width):
                print ("#", end="")
            print()
            
    def __str__(self):
        """Returns '[Rectangle] (<id>) <x>/<y> - <width>/<height>'"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"
