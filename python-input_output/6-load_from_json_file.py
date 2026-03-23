#!/usr/bin/python3
"""Module pour charger un objet depuis un fichier JSON."""
import json


def load_from_json_file(filename):
    """Crée un objet Python à partir d'un fichier JSON.

    Args:
        filename: Le nom du fichier JSON à lire.

    Returns:
        L'objet Python (list, dict, etc.) désérialisé depuis le JSON.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
