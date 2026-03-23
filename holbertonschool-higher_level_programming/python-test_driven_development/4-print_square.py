#!/usr/bin/python3
"""
Ce module contient une fonction qui imprime un
carré d'une taille donnée
en utilisant le caractère #.
"""


def print_square(size):
    """
    Args:
        size: La taille du côté du carré (doit être un entier >= 0)

    Raises:
        TypeError: Si size n'est pas un entier
        ValueError: Si size est inférieur à 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
