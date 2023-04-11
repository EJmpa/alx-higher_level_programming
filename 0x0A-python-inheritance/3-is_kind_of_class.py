#!/usr/bin/python3
"""To check if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class
"""
def is_kind_of_class(obj, a_class):
    """Return `'True'` the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class, otherwise return false
    """
    return isinstance(obj, a_class)
