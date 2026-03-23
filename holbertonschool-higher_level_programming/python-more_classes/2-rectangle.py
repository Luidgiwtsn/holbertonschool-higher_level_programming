#!/usr/bin/python3
"""Module qui définit une classe Rectangle."""


class Rectangle:
    """Classe qui représente un rectangle.

    Attributes:
        width (int): La largeur du rectangle.
        height (int): La hauteur du rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialise un nouveau Rectangle.

        Args:
            width (int, optional): La largeur du rectangle. Par défaut à 0.
            height (int, optional): La hauteur du rectangle. Par défaut à 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupère la largeur du rectangle.

        Returns:
            int: La largeur du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle.

        Args:
            value (int): La nouvelle largeur.

        Raises:
            TypeError: Si la largeur n'est pas un entier.
            ValueError: Si la largeur est inférieure à 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur du rectangle.

        Returns:
            int: La hauteur du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur du rectangle.

        Args:
            value (int): La nouvelle hauteur.

        Raises:
            TypeError: Si la hauteur n'est pas un entier.
            ValueError: Si la hauteur est inférieure à 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcule l'aire du rectangle.

        Returns:
            int: L'aire du rectangle (largeur * hauteur).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calcule le périmètre du rectangle.

        Returns:
            int: Le périmètre du rectangle.
                 Si la largeur ou la hauteur est 0, retourne 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
