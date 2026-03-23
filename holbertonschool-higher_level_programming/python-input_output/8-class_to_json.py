#!/usr/bin/python3
"""
Module qui contient la fonction class_to_json.
"""


def class_to_json(obj):
    """
    Retourne la description d'un dictionnaire pour la sérialisation JSON.

    Cette fonction convertit un objet en dictionnaire contenant tous ses
    attributs sérialisables (list, dictionary, string, integer, boolean).

    Args:
        obj: Une instance d'une classe dont tous les attributs sont
             sérialisables.

    Returns:
        dict: Un dictionnaire contenant tous les attributs de l'objet.
              Les clés sont les noms des attributs et les valeurs sont
              les valeurs des attributs.
    """
    return obj.__dict__
