#!/usr/bin/python3
"""Module contenant la fonction write_file.

Ce module fournit une fonction pour écrire du texte dans un fichier.
"""


def write_file(filename="", text=""):
    """Écrit une chaîne de caractères dans un fichier texte (UTF-8).

    Cette fonction crée le fichier s'il n'existe pas, ou écrase son contenu
    s'il existe déjà. Elle utilise l'encodage UTF-8 pour écrire le texte.

    Args:
        filename (str): Le nom du fichier dans lequel écrire.
                       Par défaut, une chaîne vide.
        text (str): Le texte à écrire dans le fichier.
                   Par défaut, une chaîne vide.

    Returns:
        int: Le nombre de caractères écrits dans le fichier.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
