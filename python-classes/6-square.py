#!/usr/bin/python3
"""Module définissant un carré."""


class Square:
    """Représente un carré.

    Attributes:
        size (int): La taille du côté du carré.
        position (tuple): La position du carré
        (décalage horizontal et vertical).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialise un nouveau carré.

        Args:
            size (int, optional): La taille du côté du carré. Par défaut 0.
            position (tuple, optional): La position du carré.
            Par défaut (0, 0).

        Raises:
            TypeError: Si size n'est pas un entier ou si position n'est pas
                       un tuple de 2 entiers positifs.
            ValueError: Si size est inférieur à 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Récupère la position du carré.

        Returns:
            tuple: La position du carré (décalage horizontal et vertical).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Définit la position du carré.

        Args:
            value (tuple): La nouvelle position du carré.

        Raises:
            TypeError: Si value n'est pas un tuple de 2 entiers positifs.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calcule l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré avec le caractère #.

        Si size est égal à 0, affiche une ligne vide.
        La position détermine le décalage horizontal et vertical.
        """
        if self.__size == 0:
            print()
            return

        # Affiche les lignes vides pour le décalage vertical
        for _ in range(self.__position[1]):
            print()

        # Affiche chaque ligne du carré avec le décalage horizontal
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
