#!/usr/bin/python3
"""Module définissant la classe Rectangle."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Classe Rectangle qui hérite de BaseGeometry.
    
    Cette classe représente un rectangle avec une largeur et une hauteur.
    Les dimensions doivent être des entiers positifs.
    """

    def __init__(self, width, height):
        """Initialise un rectangle avec une largeur et une hauteur.
        
        Args:
            width (int): La largeur du rectangle (doit être un entier positif).
            height (int): La hauteur du rectangle (doit être un entier positif).
        
        Raises:
            TypeError: Si width ou height n'est pas un entier.
            ValueError: Si width ou height est inférieur ou égal à 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
