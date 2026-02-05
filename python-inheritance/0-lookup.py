#!/usr/bin/python3
"""Module qui définit la fonction lookup."""


def lookup(obj):
    """Retourne la liste des attributs et méthodes disponibles d'un objet.

    Args:
        obj: L'objet à inspecter.

    Returns:
        Une liste contenant les noms de tous les attributs et méthodes
        disponibles pour l'objet.
    """
    return dir(obj)
