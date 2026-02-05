#!/usr/bin/python3
"""Module définissant la classe Square.

Ce module contient la classe Square qui hérite de Rectangle
et représente un carré avec validation des dimensions.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Classe représentant un carré.

    Cette classe hérite de Rectangle et implémente un carré
    où tous les côtés ont la même dimension.

    Attributes:
        __size (int): La taille du carré (attribut privé).
    """

    def __init__(self, size):
        """Initialise un nouveau carré.

        Args:
            size (int): La taille du carré (doit être un entier positif).

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size n'est pas positif.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calcule l'aire du carré.

        Returns:
            int: L'aire du carré (size * size).
        """
        return self.__size * self.__size
