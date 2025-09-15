#!/usr/bin/python3
"""Define a class Square whit private attribute size

"""
class Square:
    """Represents a square."""

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the side of the square.
                        No type or value validation is performed at this stage.
        """
        self.__size = size
