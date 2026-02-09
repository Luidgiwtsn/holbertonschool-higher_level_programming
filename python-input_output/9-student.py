#!/usr/bin/python3
"""Module qui définit la classe Student"""


class Student:
    """Classe qui représente un étudiant

    Attributes:
        first_name (str): Le prénom de l'étudiant
        last_name (str): Le nom de famille de l'étudiant
        age (int): L'âge de l'étudiant
    """

    def __init__(self, first_name, last_name, age):
        """Initialise un nouvel étudiant

        Args:
            first_name (str): Le prénom de l'étudiant
            last_name (str): Le nom de famille de l'étudiant
            age (int): L'âge de l'étudiant
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retourne la représentation dictionnaire de l'étudiant

        Returns:
            dict: Dictionnaire contenant tous les attributs de l'instance
        """
        return self.__dict__
