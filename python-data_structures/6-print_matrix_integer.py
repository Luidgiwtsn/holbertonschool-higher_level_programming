#!/usr/bin/python3
"""Module for printing a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers.

    Args:
        matrix: A list of lists containing integers. Defaults to [[]].

    Returns:
        None
    """
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
