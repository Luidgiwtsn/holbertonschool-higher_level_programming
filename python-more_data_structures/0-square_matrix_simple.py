#!/usr/bin/python3
"""Module qui calcule le carré de tous les entiers d'une matrice."""


def square_matrix_simple(matrix=[]):
    """
    Calcule le carré de tous les entiers d'une matrice.

    Args:
        matrix: Un tableau à 2 dimensions d'entiers.

    Returns:
        Une nouvelle matrice de même taille où chaque valeur est le carré
        de la valeur correspondante dans la matrice d'entrée.
    """
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num ** 2)
        new_matrix.append(new_row)
    return new_matrix
