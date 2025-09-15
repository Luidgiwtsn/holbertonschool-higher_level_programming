#!/usr/bin/python3
"""Module 0-square
Defines an empty class Square.
"""

class Square:
    """
    Represents a square."""

def __init__(self, size=0):
    """
    Initializes the square with a given size.
    Args:
        size (int): The size of the square (default is 0).
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size 

def area(self):
    """ Calculate and return the area of the square.Returns:
    Returns:
        int: The area of the square (size squared).
    """
    return self.__size * self.__size
