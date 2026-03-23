#!/usr/bin/python3
"""Module qui définit une classe Rectangle."""


class Rectangle:
    """Représente un rectangle.

    Attributs:
        number_of_instances (int): Le nombre d'instances de Rectangle.
        print_symbol: Symbole utilisé pour la représentation en chaîne.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise un nouveau Rectangle.

        Args:
            width (int): La largeur du nouveau rectangle.
            height (int): La hauteur du nouveau rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Récupère/définit la largeur du Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère/définit la hauteur du Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l'aire du Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre du Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne la représentation affichable du Rectangle.

        Représente le rectangle avec le(s) caractère(s) dans print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append(str(self.print_symbol))
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Retourne la représentation en chaîne du Rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Affiche un message à chaque suppression d'un Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
