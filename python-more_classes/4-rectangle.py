#!/usr/bin/python3
"""Module qui définit une classe Rectangle."""


class Rectangle:
    """Une classe qui définit un rectangle.

    Attributs:
        width (int): La largeur du rectangle.
        height (int): La hauteur du rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialise un nouveau Rectangle.

        Args:
            width (int): La largeur du rectangle. Par défaut 0.
            height (int): La hauteur du rectangle. Par défaut 0.
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
            value (int): La valeur de largeur à définir.

        Raises:
            TypeError: Si width n'est pas un entier.
            ValueError: Si width est inférieur à 0.
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
            value (int): La valeur de hauteur à définir.

        Raises:
            TypeError: Si height n'est pas un entier.
            ValueError: Si height est inférieur à 0.
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
            int: Le périmètre du rectangle, ou 0 si largeur ou hauteur est 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne une représentation du rectangle avec des caractères '#'.

        Returns:
            str: Le rectangle dessiné avec des caractères '#', ou une chaîne
                 vide si largeur ou hauteur est 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append("#" * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        """Retourne une représentation du rectangle pour reproduction.

        Returns:
            str: Une chaîne utilisable avec eval() pour créer une nouvelle
                 instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"
