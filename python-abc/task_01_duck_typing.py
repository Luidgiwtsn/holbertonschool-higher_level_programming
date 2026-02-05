#!/usr/bin/env python3
"""
Module de démonstration du duck typing avec des formes géométriques.

Ce module définit une classe abstraite Shape et deux implémentations
concrètes : Circle et Rectangle. Il démontre le concept de duck typing
à travers la fonction shape_info.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Classe abstraite représentant une forme géométrique.

    Cette classe sert de base pour toutes les formes géométriques
    et définit l'interface que chaque forme doit implémenter.
    """

    @abstractmethod
    def area(self):
        """
        Calcule l'aire de la forme.

        Returns:
            float: L'aire de la forme.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calcule le périmètre de la forme.

        Returns:
            float: Le périmètre de la forme.
        """
        pass


class Circle(Shape):
    """
    Classe représentant un cercle.

    Attributes:
        radius (float): Le rayon du cercle.
    """

    def __init__(self, radius):
        """
        Initialise un cercle avec un rayon donné.

        Args:
            radius (float): Le rayon du cercle.
        """
        self.radius = abs(radius)

    def area(self):
        """
        Calcule l'aire du cercle.

        Returns:
            float: L'aire du cercle (π * r²).
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calcule le périmètre du cercle.

        Returns:
            float: Le périmètre du cercle (2 * π * r).
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Classe représentant un rectangle.

    Attributes:
        width (float): La largeur du rectangle.
        height (float): La hauteur du rectangle.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur données.

        Args:
            width (float): La largeur du rectangle.
            height (float): La hauteur du rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            float: L'aire du rectangle (largeur * hauteur).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            float: Le périmètre du rectangle (2 * (largeur + hauteur)).
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Affiche les informations d'une forme (aire et périmètre).

    Cette fonction utilise le duck typing : elle ne vérifie pas
    explicitement le type de l'objet, mais suppose simplement que
    l'objet possède les méthodes area() et perimeter().

    Args:
        shape: Un objet possédant les méthodes area() et perimeter().
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
