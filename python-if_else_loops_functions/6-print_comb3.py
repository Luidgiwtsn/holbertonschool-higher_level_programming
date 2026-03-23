#!/usr/bin/python3
"""
Imprime toutes les combinaisons possibles de deux chiffres différents.

Les nombres sont séparés par ', ', les deux chiffres doivent être
différents et seule la plus petite combinaison de chaque paire est
affichée. L'ordre est croissant et chaque nombre est affiché avec
deux chiffres. Le dernier nombre est suivi d'un retour à la ligne.
"""

for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}, ".format(i, j), end="")
