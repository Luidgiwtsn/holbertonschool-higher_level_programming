#!/usr/bin/python3
"""
Ce module contient une fonction pour ajouter du texte à la fin d'un fichier.
"""


def append_write(filename="", text=""):
    """
    Ajoute une chaîne de caractères à la fin d'un fichier texte UTF-8.

    Args:
        filename (str): Le nom du fichier dans lequel écrire.
        text (str): Le texte à ajouter à la fin du fichier.

    Returns:
        int: Le nombre de caractères ajoutés au fichier.

    Note:
        Si le fichier n'existe pas, il sera créé automatiquement.
        Utilise l'instruction 'with' pour gérer le fichier en toute sécurité.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
