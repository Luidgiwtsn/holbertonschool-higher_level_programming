#!/usr/bin/python3
"""Module pour la division de matrice.

Ce module contient une fonction qui divise tous les éléments d'une matrice.
"""


def matrix_divided(matrix, div):
    """Divise tous les éléments d'une matrice par un nombre donné.

    Args:
        matrix: Une liste de listes d'entiers ou de flottants.
        div: Le nombre par lequel diviser (entier ou flottant).

    Returns:
        Une nouvelle matrice avec tous les éléments divisés par div,
        arrondis à 2 décimales.

    Raises:
        TypeError: Si matrix n'est pas une liste de listes d'entiers/flottants.
        TypeError: Si les lignes de la matrice ont des tailles différentes.
        TypeError: Si div n'est pas un nombre.
        ZeroDivisionError: Si div est égal à 0."""

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(error_msg)

    for row in matrix:
        if len(row) == 0:
            raise TypeError(error_msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
