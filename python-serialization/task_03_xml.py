#!/usr/bin/env python3
"""
Module de sérialisation et désérialisation XML.

Ce module fournit des fonctions pour convertir des dictionnaires Python
en fichiers XML et vice versa.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python en XML et l'enregistre dans un fichier.

    Args:
        dictionary (dict): Le dictionnaire à sérialiser.
        filename (str): Le nom du fichier XML de destination.

    Returns:
        None
    """
    # Créer l'élément racine
    root = ET.Element('data')

    # Itérer sur les éléments du dictionnaire
    for key, value in dictionary.items():
        # Créer un sous-élément pour chaque paire clé-valeur
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Créer l'arbre XML
    tree = ET.ElementTree(root)

    # Indenter le XML pour une meilleure lisibilité
    ET.indent(tree, space='    ')

    # Écrire l'arbre dans le fichier
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML en dictionnaire Python.

    Args:
        filename (str): Le nom du fichier XML à lire.

    Returns:
        dict: Le dictionnaire reconstruit à partir du XML.
    """
    # Parser le fichier XML
    tree = ET.parse(filename)
    root = tree.getroot()

    # Créer un dictionnaire vide
    dictionary = {}

    # Itérer sur les éléments enfants
    for child in root:
        # Ajouter chaque élément au dictionnaire
        dictionary[child.tag] = child.text

    return dictionary
