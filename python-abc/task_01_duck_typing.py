#!/usr/bin/env python3
"""
Defines abstract and concrete shepe classes
and a function to display their area and perimeter
using duck typing.
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    All subclasses must implement area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape class inheriting from Shape.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance with the given radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate and return the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape class inheriting from Shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Display the area and perimeter of the shape passed in.

    Args:
        shape: Any object with area() and perimeter() methods (duck typing).
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
