#!/usr/bin/python3
"""Module pour sauvegarder un objet Python dans un fichier JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Écrit un objet dans un fichier texte en utilisant JSON.

    Args:
        my_obj: L'objet Python à sauvegarder (list, dict, str, int, etc.)
        filename (str): Le nom du fichier où sauvegarder l'objet

    Returns:
        None

    Note:
        Cette fonction ne gère pas les exceptions si l'objet n'est pas
        sérialisable en JSON ou si des erreurs de permissions surviennent.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
