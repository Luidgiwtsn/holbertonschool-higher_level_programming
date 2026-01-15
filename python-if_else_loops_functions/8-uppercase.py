#!/usr/bin/env python3
"""
Module qui définit une fonction pour afficher une chaîne en majuscules.
"""


def uppercase(str):
    """
    Affiche une chaîne de caractères en majuscules suivie d'un retour à la ligne.

    Args:
        str (str): La chaîne à convertir en majuscules.
    """
    resultat = ""
    for char in str:
        # Vérifie si le caractère est une lettre minuscule
        if 97 <= ord(char) <= 122:
            # Convertit en majuscule en soustrayant 32
            resultat += chr(ord(char) - 32)
        else:
            resultat += char
    print("{}".format(resultat))
