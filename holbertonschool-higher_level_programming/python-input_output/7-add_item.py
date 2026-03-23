#!/usr/bin/python3
"""
Module qui ajoute tous les arguments à une liste Python et les sauvegarde.

Ce script utilise les fonctions save_to_json_file et load_from_json_file
pour gérer une liste persistante d'éléments dans un fichier JSON.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    ma_liste = load_from_json_file(filename)
except FileNotFoundError:
    ma_liste = []

ma_liste.extend(sys.argv[1:])
save_to_json_file(ma_liste, filename)
