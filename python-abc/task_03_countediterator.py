#!/usr/bin/env python3
"""
Module définissant la classe CountedIterator.

Ce module fournit une classe qui étend les fonctionnalités d'un itérateur
standard en ajoutant un compteur pour suivre le nombre d'éléments itérés.
"""


class CountedIterator:
    """
    Itérateur avec compteur intégré.

    Cette classe encapsule un itérateur standard et garde trace du nombre
    d'éléments qui ont été parcourus lors de l'itération.

    Attributes:
        iterator: L'objet itérateur interne.
        count (int): Le nombre d'éléments itérés jusqu'à présent.
    """

    def __init__(self, iterable):
        """
        Initialise un CountedIterator.

        Args:
            iterable: Un objet itérable (liste, tuple, etc.) sur lequel
                     itérer.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Récupère l'élément suivant de l'itérateur.

        Cette méthode incrémente le compteur à chaque appel et retourne
        l'élément suivant de l'itérateur interne.

        Returns:
            Le prochain élément de la séquence.

        Raises:
            StopIteration: Lorsqu'il n'y a plus d'éléments à itérer.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Retourne le nombre d'éléments itérés.

        Returns:
            int: Le nombre total d'éléments qui ont été parcourus.
        """
        return self.count

    def __iter__(self):
        """
        Retourne l'itérateur lui-même.

        Cette méthode permet à CountedIterator d'être utilisé dans des
        boucles for et autres contextes d'itération.

        Returns:
            self: L'instance elle-même.
        """
        return self
