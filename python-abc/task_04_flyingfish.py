#!/usr/bin/env python3
"""
Module démonstrant l'héritage multiple en Python.

Ce module contient trois classes :
- Fish : classe représentant un poisson
- Bird : classe représentant un oiseau
- FlyingFish : classe héritant de Fish et Bird, représentant un poisson volant

L'objectif est de comprendre le MRO (Method Resolution Order) en Python.
"""


class Fish:
    """
    Classe représentant un poisson.

    Cette classe définit les comportements de base d'un poisson,
    notamment la nage et son habitat naturel.
    """

    def swim(self):
        """Affiche que le poisson nage."""
        print("The fish is swimming")

    def habitat(self):
        """Affiche l'habitat du poisson."""
        print("The fish lives in water")


class Bird:
    """
    Classe représentant un oiseau.

    Cette classe définit les comportements de base d'un oiseau,
    notamment le vol et son habitat naturel.
    """

    def fly(self):
        """Affiche que l'oiseau vole."""
        print("The bird is flying")

    def habitat(self):
        """Affiche l'habitat de l'oiseau."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Classe représentant un poisson volant.

    Cette classe hérite à la fois de Fish et de Bird, démontrant
    l'héritage multiple en Python. Elle redéfinit les méthodes
    des deux classes parentes pour adapter le comportement
    spécifique au poisson volant.

    L'ordre d'héritage (Fish, Bird) influence le MRO (Method Resolution Order).
    """

    def swim(self):
        """Affiche que le poisson volant nage."""
        print("The flying fish is swimming!")

    def fly(self):
        """Affiche que le poisson volant plane."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Affiche l'habitat du poisson volant."""
        print("The flying fish lives both in water and the sky!")
