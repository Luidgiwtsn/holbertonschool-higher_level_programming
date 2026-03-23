#!/usr/bin/python3
"""Module qui définit une classe Square avec propriété size et validation."""


class Square:
    """Une classe qui représente un carré.

    Cette classe définit un carré avec un attribut privé size,
    avec validation via des getters et setters de propriété.

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
        self.size = size

    @property
    def size(self):
        """Récupère la taille du carré.

        Returns:
            int: La taille du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille du carré.

        Args:
            value (int): La nouvelle taille du carré.

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
        """Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré (size * size).
        """
        return self.__size ** 2
