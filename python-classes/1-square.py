#!/usr/bin/python3
"""Module qui définit une classe Square."""


class Square:
    """Une classe qui définit un carré par sa taille.

    Attributes:
        __size: Attribut privé représentant la taille du carré.
    """

    def __init__(self, size):
        """Initialise une nouvelle instance de Square.

        Args:
            size: La taille du carré (sans vérification de type/valeur).
        """
        self.__size = size
