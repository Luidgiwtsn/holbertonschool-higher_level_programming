#!/usr/bin/python3
"""
Module pour additionner deux entiers.
Ce module fournit une fonction pour additionner deux nombres
après les avoir convertis en entiers s'ils sont des flottants.
"""


def add_integer(a, b=98):
    """Additionne deux entiers après conversion si nécessaire.
    Retourne la somme de a et b.
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
