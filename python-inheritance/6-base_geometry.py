#!/usr/bin/python3
"""Module définissant la classe BaseGeometry.

Ce module contient la classe BaseGeometry qui sert de classe de base
pour les opérations géométriques.
"""


class BaseGeometry:
    """Classe de base pour les opérations géométriques.

    Cette classe définit une interface pour les calculs géométriques
    avec une méthode area() qui doit être implémentée par les sous-classes.
    """

    def area(self):
        """Calcule l'aire de la forme géométrique.

        Cette méthode doit être implémentée par les classes dérivées.

        Raises:
            Exception: Toujours levée avec le message
                      'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
