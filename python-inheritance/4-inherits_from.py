#!/usr/bin/python3
"""
Module qui définit la fonction inherits_from.

Ce module contient une fonction permettant de vérifier si un objet
est une instance d'une classe qui hérite (directement ou indirectement)
d'une classe spécifiée.
"""


def inherits_from(obj, a_class):
    """
    Vérifie si un objet est une instance d'une classe qui hérite
    (directement ou indirectement) de la classe spécifiée.

    Cette fonction retourne True si l'objet est une instance d'une classe
    qui est une sous-classe de a_class, mais pas si l'objet est une instance
    directe de a_class elle-même.

    Args:
        obj: L'objet à vérifier.
        a_class: La classe parente à vérifier.

    Returns:
        bool: True si obj est une instance d'une sous-classe de a_class,
              False sinon
              (y compris si obj est une instance directe de a_class).
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
