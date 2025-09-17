#!/usr/bin/python3
"""
This defines a Rectangle class that models a rectangle
with width and height, and provides methods for area, perimeter,
and string representation.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.

    Provides methods to calculate area, perimeter,
    and string representations using '#' characters.
    """


    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle (default 0).
            height (int): Height of the rectangle (default 0).
        """
        self.width = width
        self.height = height


    @property
    def width(self):
        """
        Getter for the width of the rectangle.

        Args:
            width (int): Width of the rectangle (default 0).
            height (int): Height of the rectangle (default 0).
        """
        return self.__width


    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.

        Args:
            value (int): New width to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height


    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.

        Args:
            value (int): New height to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter (2 * (width + height)),
            or 0 if either width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return the string representation of the rectangle using '#'.

        Returns:
            str: The rectangle drawn with '#' characters.
        """
        if self.width == 0 or self.height == 0:
            return ""
        lines = []
        for _ in range(self.height):
            lines.append('#' * self.width)
        return '\n'.join(lines)

    def __repr__(self):
        """
        Return an official string representation that can recreate the object.

        Returns:
            str: String in the format Rectangle(width, height).
        """
        return f"Rectangle({self.width}, {self.height})"
