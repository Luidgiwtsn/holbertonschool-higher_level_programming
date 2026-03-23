#!/usr/bin/python3
"""
Ce module contient une fonction qui vérifie si un objet est une instance
d'une classe ou d'une classe qui en hérite.
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si un objet est une instance d'une classe spécifiée
    ou d'une classe qui en hérite.

    Args:
        obj: L'objet à vérifier
        a_class: La classe à comparer

    Returns:
        True si obj est une instance de a_class ou d'une classe
        qui hérite de a_class, False sinon
    """
    return isinstance(obj, a_class)
