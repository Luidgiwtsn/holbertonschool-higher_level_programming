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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (length of one side).
            Defaults to 0.

        Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
            """Get the position of the square."""
            return self.__position

    @position.setter
    def position(self, value):
            """
            Sets the position of the square with validation.

            Args:
                value (tuple): The new position value.

            Raises:
                TypeError: If value is not a tuple of 2 positive integers.
            """
            if (not isinstance(value, tuple) or len(value) != 2 or
                    not all(isinstance(num, int) for num in value) or
                    not all(num >= 0 for num in value)):
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character, considering its position.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print the vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print the square rows
        for _ in range(self.__size):
            # Print the horizontal offset
            print(" " * self.__position[0], end="")
            # Print the square row
            print("#" * self.__size)
