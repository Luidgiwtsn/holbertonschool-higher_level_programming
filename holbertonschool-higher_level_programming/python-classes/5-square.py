#!/usr/bin/python3
"""Module qui définit une classe Square (carré)."""


class Square:
    """Classe qui représente un carré.

    Attributes:
        __size (int): La taille du côté du carré (privé).
    """

    def __init__(self, size=0):
        """Initialise un nouveau carré.

        Args:
            size (int, optional): La taille du côté du carré. Par défaut 0.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        self.size = size

    @property
    def size(self):
        """Récupère la taille du carré.

        Returns:
            int: La taille du côté du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille du carré.

        Args:
            value (int): La nouvelle taille du côté du carré.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcule l'aire du carré.

        Returns:
            int: L'aire du carré (taille * taille).
        """
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré avec le caractère #.

        Si la taille est 0, affiche une ligne vide.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
