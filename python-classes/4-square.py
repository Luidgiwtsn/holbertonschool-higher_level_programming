#!/usr/bin/python3
"""
This defines a class that represents a square.

The Square class allows for instantiation with a size, validates the input,
and provides a method to compute the area of the square.
"""

class Square:
    """
    Represents a geometric square.
    The Square class encapsulates the concept of a square by maintaining
    a private size attribute and providing a method to compute its area.
    """
    
    def __init__(self, size=0):
    """
    Initialize a new Square instance.

    Args:
        size (int): The size of the square (length of one side). Defaults to 0.

    Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
    """ 
    self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
def area(self):
        """
        Compute the area of the square.
        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
