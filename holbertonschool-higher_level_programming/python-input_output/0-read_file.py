#!/usr/bin/python3
"""Module pour lire et afficher le contenu d'un fichier."""


def read_file(filename=""):
    """
    Lit un fichier texte UTF-8 et affiche son contenu sur stdout.

    Args:
        filename (str): Le chemin du fichier à lire. Par défaut une
                        chaîne vide.

    Cette fonction utilise le gestionnaire de contexte 'with' pour
    ouvrir le fichier en toute sécurité. Le fichier est ouvert en
    mode lecture avec l'encodage UTF-8.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
