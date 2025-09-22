#!/usr/bin/python3
"""
Defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    Represents base geometry.
    """

    def area(self):
        """
        Raises:
            Exception: always, with message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
