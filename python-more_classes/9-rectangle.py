#!/usr/bin/python3
"""Module qui définit une classe Rectangle."""


class Rectangle:
    """Classe qui définit un rectangle.

    Attributs de classe:
        number_of_instances (int): Nombre d'instances de Rectangle.
        print_symbol: Symbole utilisé pour la représentation en chaîne.

    Attributs d'instance:
        width (int): Largeur du rectangle.
        height (int): Hauteur du rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise un nouveau rectangle.

        Args:
            width (int, optionnel): Largeur du rectangle. Par défaut 0.
            height (int, optionnel): Hauteur du rectangle. Par défaut 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            value (int): La nouvelle hauteur.

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
            int: L'aire du rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calcule le périmètre du rectangle.

        Returns:
            int: Le périmètre du rectangle, ou 0 si width ou height vaut 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne une représentation en chaîne du rectangle.

        Returns:
            str: Le rectangle dessiné avec le symbole print_symbol,
                 ou une chaîne vide si width ou height vaut 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for i in range(self.__height):
            rectangle.append(str(self.print_symbol) * self.__width)
        return "\n".join(rectangle)

    def __repr__(self):
        """Retourne une représentation du rectangle pour eval().

        Returns:
            str: Une chaîne permettant de recréer l'instance avec eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Détruit une instance de Rectangle.

        Affiche un message et décrémente le compteur d'instances.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Retourne le plus grand rectangle basé sur l'aire.

        Args:
            rect_1 (Rectangle): Le premier rectangle.
            rect_2 (Rectangle): Le deuxième rectangle.

        Returns:
            Rectangle: Le rectangle avec la plus grande aire,
                       ou rect_1 si les aires sont égales.

        Raises:
            TypeError: Si rect_1 ou rect_2 n'est pas une instance de Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Crée un carré (rectangle avec width == height).

        Args:
            size (int, optionnel): La taille du côté du carré. Par défaut 0.

        Returns:
            Rectangle: Une nouvelle instance de Rectangle avec width == height.
        """
        return cls(size, size)
