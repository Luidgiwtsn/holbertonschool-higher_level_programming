#!/usr/bin/env python3
"""
Module de conversion CSV vers JSON.

Ce module fournit une fonction pour convertir un fichier CSV
en format JSON en utilisant les techniques de sérialisation.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convertit un fichier CSV en format JSON.

    Cette fonction lit les données d'un fichier CSV et les convertit
    en format JSON. Chaque ligne du CSV devient un objet JSON dans
    un tableau. Les données sont écrites dans le fichier 'data.json'.

    Args:
        csv_filename (str): Le nom du fichier CSV à convertir.

    Returns:
        bool: True si la conversion a réussi, False en cas d'erreur
              (par exemple, si le fichier n'est pas trouvé).

    Note:
        Le fichier de sortie est toujours nommé 'data.json'.
        Les valeurs du CSV sont conservées comme chaînes de caractères.
    """
    try:
        # Ouvrir et lire le fichier CSV
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # Utiliser DictReader pour convertir chaque ligne en dictionnaire
            csv_reader = csv.DictReader(csv_file)
            
            # Convertir l'objet DictReader en liste de dictionnaires
            data = list(csv_reader)
        
        # Sérialiser et écrire les données en JSON
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    
    except FileNotFoundError:
        # Gérer l'erreur si le fichier CSV n'existe pas
        return False
    except Exception:
        # Gérer toute autre exception
        return False
