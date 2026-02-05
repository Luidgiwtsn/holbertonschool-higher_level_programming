#!/usr/bin/python3
"""Module qui définit la fonction is_same_class.

Ce module contient une fonction pour vérifier si un objet est exactement
une instance d'une classe spécifiée (pas une sous-classe).
"""


def is_same_class(obj, a_class):
    """Vérifie si un objet est exactement une instance d'une classe donnée.

    Cette fonction retourne True si l'objet est une instance exacte de la
    classe spécifiée, False sinon. Elle ne retourne pas True pour les
    instances de sous-classes.

    Args:
        obj: L'objet à vérifier.
        a_class: La classe à comparer avec le type de l'objet.

    Returns:
        bool: True si obj est exactement une instance de a_class,
              False sinon.
    """
    return type(obj) is a_class
