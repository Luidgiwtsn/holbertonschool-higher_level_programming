#!/usr/bin/env python3
"""
Module de sérialisation basique pour les dictionnaires Python vers JSON.

Ce module fournit des fonctionnalités pour sérialiser des dictionnaires
Python vers des fichiers JSON et désérialiser des fichiers JSON pour
recréer des dictionnaires Python.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python en JSON et le sauvegarde dans un fichier.

    Cette fonction prend un dictionnaire Python et l'écrit dans un fichier
    au format JSON. Si le fichier existe déjà, il sera remplacé.

    Args:
        data (dict): Un dictionnaire Python contenant les données à sérialiser.
        filename (str): Le nom du fichier JSON de sortie.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Charge et désérialise les données d'un fichier JSON vers un dictionnaire.

    Cette fonction lit un fichier JSON et convertit son contenu en un
    dictionnaire Python.

    Args:
        filename (str): Le nom du fichier JSON d'entrée.

    Returns:
        dict: Un dictionnaire Python contenant les données désérialisées
              du fichier JSON.
    """
    with open(filename, 'r') as file:
        return json.load(file)
