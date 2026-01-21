#!/usr/bin/python3
"""
Module pour additionner deux entiers.

Ce module fournit une fonction pour additionner deux nombres
après les avoir convertis en entiers s'ils sont des flottants.
"""


def add_integer(a, b=98):
    """
    Additionne deux entiers.

    Args:
        a: Premier nombre (int ou float)
        b: Deuxième nombre (int ou float), 98 par défaut

    Returns:
        int: La somme de a et b en tant qu'entiers

    Raises:
        TypeError: Si a ou b ne sont pas des entiers ou des flottants
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
