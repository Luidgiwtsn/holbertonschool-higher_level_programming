#!/usr/bin/python3
"""Module définissant la classe Student."""


class Student:
    """Classe représentant un étudiant.

    Attributs publics d'instance:
        first_name (str): Le prénom de l'étudiant.
        last_name (str): Le nom de famille de l'étudiant.
        age (int): L'âge de l'étudiant.
    """

    def __init__(self, first_name, last_name, age):
        """Initialise une nouvelle instance de Student.

        Args:
            first_name (str): Le prénom de l'étudiant.
            last_name (str): Le nom de famille de l'étudiant.
            age (int): L'âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Récupère la représentation en dictionnaire de l'instance Student.

        Si attrs est une liste de chaînes de caractères, seuls les attributs
        dont le nom figure dans cette liste sont récupérés.
        Dans tous les autres cas, tous les attributs sont récupérés.

        Args:
            attrs (list, optional): Liste de noms d'attributs à récupérer.
                Par défaut None (tous les attributs sont récupérés).

        Returns:
            dict: Dictionnaire contenant les attributs demandés de l'instance.
        """
        if isinstance(attrs, list) and all(
            isinstance(a, str) for a in attrs
        ):
            return {
                k: v for k, v in self.__dict__.items() if k in attrs
            }
        return self.__dict__
