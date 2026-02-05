#!/usr/bin/python3
"""Module définissant la classe BaseGeometry.

Ce module contient la classe BaseGeometry qui sert de classe de base
pour les formes géométriques avec validation des valeurs.
"""


class BaseGeometry:
    """Classe de base pour les opérations géométriques.

    Cette classe fournit des méthodes de base pour les calculs
    géométriques et la validation des valeurs entières.
    """

    def area(self):
        """Calcule l'aire de la forme géométrique.

        Raises:
            Exception: Cette méthode n'est pas encore implémentée.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide qu'une valeur est un entier positif.

        Args:
            name (str): Le nom de la valeur à valider.
            value: La valeur à valider.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur ou égal à 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
