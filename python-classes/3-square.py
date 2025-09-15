#!/usr/bin/python3
"""
This module defines a class that represents a square.

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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
