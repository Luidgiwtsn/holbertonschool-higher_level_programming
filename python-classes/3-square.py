#!/usr/bin/python3
"""
This module defines a class Square that represents a square and provides
a method to compute its area. It validates input to ensure only non-negative
integers can be used as the size of the square.
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

def Area(self):
    """ 
    Calculate and return the area of the square.Returns:
    
    Returns:
        int: The area of the square (size squared).
    """
    return self.__size ** 2
