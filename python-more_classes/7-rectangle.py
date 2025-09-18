#!/usr/bin/python3
"""
This defines a Rectangle class that represents a geometric rectangle.
It includes methods for computing area, perimeter, and string representation.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.
    Tracks the number of instances and supports customizable string symbols.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter (2 * (width + height)),
            or 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using print_symbol.

        Returns:
            str: String of symbols forming the rectangle shape.
        """
        if self.width == 0 or self.height == 0:
            return ""
        line = str(self.print_symbol) * self.width
        return "\n".join([line] * self.height)

    def __pepr__(self):
        """
        Returns a string that can be used to recreate this rectangle.

        Returns:
            str: Reproducible string representation.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Called when the rectangle instance is deleted.
        Prints a goodbye message and decrements instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
