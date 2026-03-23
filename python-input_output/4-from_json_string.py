#!/usr/bin/python3
"""Module pour convertir une chaîne JSON en objet Python."""
import json


def from_json_string(my_str):
    """Retourne un objet Python représenté par une chaîne JSON.

    Args:
        my_str (str): Chaîne de caractères au format JSON.

    Returns:
        object: Objet Python (dict, list, etc.) correspondant au JSON.
    """
    return json.loads(my_str)
