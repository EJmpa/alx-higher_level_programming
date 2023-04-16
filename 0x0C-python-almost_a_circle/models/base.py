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


