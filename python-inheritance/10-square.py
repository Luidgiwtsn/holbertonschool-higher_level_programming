#!/usr/bin/python3
"""Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: area (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return the string representation of the square.

        Returns:
            str: formatted square description.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
