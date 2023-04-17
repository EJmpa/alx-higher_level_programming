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
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
        
    def update(self, *args, **kwargs):
        """A method that updates attributes by assigning
        an argument to each of them
        """
        if (args is not None) and len(args) != 0:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                if i == 1:
                    self.size = value
                if i == 2:
                    self.x = value
                if i == 3:
                    self.y = value
                i += 1
                
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
