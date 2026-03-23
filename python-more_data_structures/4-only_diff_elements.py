#!/usr/bin/python3
"""Module contenant une fonction pour trouver la différence symétrique."""


def only_diff_elements(set_1, set_2):
    """Retourne un ensemble d'éléments présents dans
    un seul des deux ensembles.

    Args:
        set_1: Premier ensemble
        set_2: Deuxième ensemble

    Returns:
        Un ensemble contenant les éléments présents dans set_1 ou set_2,
        mais pas dans les deux
    """
    return set_1 ^ set_2
