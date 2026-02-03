#!/usr/bin/python3
"""Module qui définit la classe Square.

Ce module contient la classe Square qui hérite de Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Classe représentant un carré.

    Cette classe hérite de Rectangle et représente un carré
    avec tous les côtés de même taille.

    Attributes:
        __size (int): La taille du carré (privé).
    """

    def __init__(self, size):
        """Initialise un nouveau carré.

        Args:
            size (int): La taille du carré (doit être un entier positif).

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur ou égal à 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """Retourne la représentation en chaîne du carré.

        Returns:
            str: Description du carré au format [Square] <width>/<height>.
        """
        return f"[Square] {self.__size}/{self.__size}"
