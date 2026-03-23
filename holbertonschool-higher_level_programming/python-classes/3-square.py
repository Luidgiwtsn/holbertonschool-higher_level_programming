#!/usr/bin/python3
"""Module qui définit une classe Square (Carré)."""


class Square:
    """Une classe qui représente un carré.

    Attributes:
        __size (int): La taille du carré (privé).
    """

    def __init__(self, size=0):
        """Initialise une nouvelle instance de Square.

        Args:
            size (int, optional): La taille du carré. Par défaut 0.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré (size * size).
        """
        return self.__size ** 2
