#!/usr/bin/python3
"""Module qui définit une classe Rectangle."""


class Rectangle:
    """Représente un rectangle.

    Attributs:
        width (int): La largeur du rectangle.
        height (int): La hauteur du rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialise un nouveau Rectangle.

        Args:
            width (int): La largeur du nouveau rectangle.
            height (int): La hauteur du nouveau rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupère la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle.

        Args:
            value (int): La valeur de la largeur.

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
        """Récupère la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur du rectangle.

        Args:
            value (int): La valeur de la hauteur.

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
        """Retourne l'aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre du rectangle.

        Si width ou height est 0, le périmètre est 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne une représentation en chaîne du rectangle avec '#'.
        Si width ou height est 0, retourne une chaîne vide.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for i in range(self.__height):
            rectangle.append("#" * self.__width)
        return "\n".join(rectangle)

    def __repr__(self):
        """Retourne une représentation pour recréer le rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Affiche un message quand une instance de Rectangle est supprimée."""
        print("Bye rectangle...")
