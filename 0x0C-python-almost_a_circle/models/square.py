"""A Module that of a class `'Sqaure'` that inherits `'Rectangle'` class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """A 'Square'` class that inherits the '`Rectangle'` class"""
    def __init__(self, size, x=0, y=0, id=None):
        """`'Square'` class initialization"""
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)
        
    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - \
{self.size}"
    
    @property
    def size(self):
        """Gets the value of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the value for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
        
    def update(self, *args, **kwargs):
        """A method that updates attributes by assigning
        an argument to each of them
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
                
        elif (kwargs is not None) and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
            """
            Returns the dictionary representation of a `'Square'`
            class attributes
            """
            d = {
                'id': self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
            }
            return d
