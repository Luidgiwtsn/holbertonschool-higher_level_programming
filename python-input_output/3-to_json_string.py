#!/usr/bin/python3
"""Module qui définit une fonction pour convertir un objet en JSON."""
import json


def to_json_string(my_obj):
    """Retourne la représentation JSON d'un objet sous forme de chaîne.

    Args:
        my_obj: L'objet Python à convertir en JSON (liste, dict, etc.).

    Returns:
        str: La représentation JSON de l'objet sous forme de chaîne.

    Note:
        Cette fonction ne gère pas les exceptions si l'objet ne peut pas
        être sérialisé en JSON.
    """
    return json.dumps(my_obj)
