#!/usr/bin/python3
"""
Module qui définit une fonction pour vérifier si un caractère est en minuscule.
"""


def islower(c):
    """
    Vérifie si un caractère est en minuscule.

    Args:
        c (str): Un seul caractère.

    Returns:
        bool: True si c est en minuscule, False sinon.
    """
    if len(c) != 1:
        return False
    return ord('a') <= ord(c) <= ord('z')
