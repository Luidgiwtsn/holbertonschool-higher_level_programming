#!/usr/bin/env python3
"""
Module pour la sérialisation et la désérialisation d'objets personnalisés.

Ce module contient la classe CustomObject qui permet de créer des objets
avec des attributs personnalisés et de les sauvegarder/charger depuis
des fichiers en utilisant le module pickle.
"""

import pickle


class CustomObject:
    """
    Classe représentant un objet personnalisé avec des attributs de base.

    Cette classe permet de créer des objets avec un nom, un âge et un statut
    d'étudiant. Elle fournit également des méthodes pour sérialiser et
    désérialiser les instances.

    Attributes:
        name (str): Le nom de l'objet/personne.
        age (int): L'âge de l'objet/personne.
        is_student (bool): Indique si l'objet/personne est étudiant(e).
    """

    def __init__(self, name, age, is_student):
        """
        Initialise une nouvelle instance de CustomObject.

        Args:
            name (str): Le nom de l'objet/personne.
            age (int): L'âge de l'objet/personne.
            is_student (bool): Statut étudiant de l'objet/personne.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet dans un format lisible.

        Cette méthode imprime le nom, l'âge et le statut étudiant
        de l'instance courante.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'instance courante dans un fichier.

        Utilise le module pickle pour sauvegarder l'objet dans un fichier
        binaire. En cas d'erreur, retourne None.

        Args:
            filename (str): Le chemin du fichier où sauvegarder l'objet.

        Returns:
            bool or None: True si la sérialisation réussit, None en cas
            d'erreur.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            return True
        except Exception as e:
            print(f"Erreur lors de la sérialisation: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet CustomObject depuis un fichier.

        Charge et retourne une instance de CustomObject depuis un fichier
        créé avec la méthode serialize(). En cas d'erreur (fichier
        inexistant, corrompu, etc.), retourne None.

        Args:
            filename (str): Le chemin du fichier à charger.

        Returns:
            CustomObject or None: L'instance désérialisée si succès,
            None en cas d'erreur.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except FileNotFoundError:
            print(f"Erreur: Le fichier '{filename}' n'existe pas.")
            return None
        except pickle.UnpicklingError:
            print(f"Erreur: Le fichier '{filename}' est corrompu ou mal formé.")
            return None
        except Exception as e:
            print(f"Erreur lors de la désérialisation: {e}")
            return None
