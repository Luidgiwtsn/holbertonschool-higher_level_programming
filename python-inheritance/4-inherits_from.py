#!/usr/bin/python3
"""
that defines a function to check if an object
is an instance of a class that inherits from a given class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
              False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
