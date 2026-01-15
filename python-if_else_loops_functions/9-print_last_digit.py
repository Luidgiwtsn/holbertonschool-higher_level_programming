#!/usr/bin/python3
"""Module qui définit une fonction pour afficher le dernier
chiffre d'un nombre."""


def print_last_digit(number):
    """
    Affiche le dernier chiffre d'un nombre et le renvoie.

    Args:
        number (int): Le nombre dont on veut obtenir le dernier chiffre.

    Returns:
        int: Le dernier chiffre du nombre.
    """
    dernier_chiffre = abs(number) % 10
    print(dernier_chiffre, end="")
    return dernier_chiffre
