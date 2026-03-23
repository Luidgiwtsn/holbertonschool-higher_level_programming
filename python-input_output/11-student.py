#!/usr/bin/python3
"""Module définissant la classe Student avec sérialisation
et désérialisation."""


class Student:
    """Classe représentant un étudiant.

    Attributs publics d'instance :
        first_name (str): Le prénom de l'étudiant.
        last_name (str): Le nom de famille de l'étudiant.
        age (int): L'âge de l'étudiant.
    """

    def __init__(self, first_name, last_name, age):
        """Initialise une instance de Student.

        Args:
            first_name (str): Le prénom de l'étudiant.
            last_name (str): Le nom de famille de l'étudiant.
            age (int): L'âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retourne une représentation dictionnaire de l'instance Student.

        Si attrs est une liste de chaînes de caractères, seuls les attributs
        dont le nom figure dans cette liste sont récupérés.
        Sinon, tous les attributs sont récupérés.

        Args:
            attrs (list, optionnel): Liste de noms d'attributs à récupérer.
                Par défaut None (tous les attributs sont retournés).

        Returns:
            dict: Dictionnaire contenant les attributs de l'instance.
        """
        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Remplace tous les attributs de l'instance Student.

        Chaque clé du dictionnaire correspond au nom d'un attribut public,
        et sa valeur associée devient la nouvelle valeur de cet attribut.

        Args:
            json (dict): Dictionnaire contenant les attributs à mettre à jour.
                Les clés sont les noms des attributs publics et les valeurs
                sont les nouvelles valeurs à assigner.
        """
        for key, value in json.items():
            setattr(self, key, value)
