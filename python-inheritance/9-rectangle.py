#!/usr/bin/python3
"""
Module qui définit la classe Rectangle.

Ce module contient la classe Rectangle qui hérite de BaseGeometry
et permet de créer des rectangles avec validation des dimensions.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe Rectangle qui hérite de BaseGeometry.

    Cette classe représente un rectangle avec une largeur et une hauteur.
    Les dimensions sont validées pour être des entiers positifs.

    Attributes:
        __width (int): La largeur du rectangle (privé).
        __height (int): La hauteur du rectangle (privé).
    """

    def __init__(self, width, height):
        """
        Initialise un nouveau rectangle.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.

        Raises:
            TypeError: Si width ou height n'est pas un entier.
            ValueError: Si width ou height est inférieur ou égal à 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.

        Returns:
            int: L'aire du rectangle (largeur * hauteur).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Retourne la représentation en chaîne du rectangle.

        Returns:
            str: La description du rectangle au
            format [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
