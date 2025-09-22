#!/usr/bin/python3
"""
Defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    Base class for geometry operations.
    """

    def area(self):
        """
        Calculate the area of the geometry.
        Raises:
            Exception: If the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer greater than 0.

        Args:
            name (str): The name of the value (used in the error message).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
