#!/usr/bin/python3
"""Module qui définit la classe MyList.

Ce module contient une classe MyList qui hérite de la classe list
et ajoute une méthode pour afficher la liste triée.
"""


class MyList(list):
    """Classe qui hérite de list avec une méthode d'affichage trié.

    Cette classe étend la classe list de Python en ajoutant
    une méthode print_sorted() qui affiche les éléments de la liste
    triés par ordre croissant sans modifier la liste originale.
    """

    def print_sorted(self):
        """Affiche la liste triée par ordre croissant.

        Cette méthode crée une copie triée de la liste et l'affiche.
        La liste originale n'est pas modifiée.
        Tous les éléments de la liste doivent être de type int.
        """
        print(sorted(self))
