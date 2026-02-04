#!/usr/bin/env python3
"""
Module définissant une classe abstraite Animal et ses sous-classes.

Ce module utilise le package ABC de Python pour créer une classe de base
abstraite Animal et deux implémentations concrètes : Dog et Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe abstraite représentant un animal.

    Cette classe sert de blueprint pour créer des classes d'animaux
    spécifiques. Toute sous-classe doit implémenter la méthode sound().
    """

    @abstractmethod
    def sound(self):
        """
        Méthode abstraite pour retourner le son de l'animal.

        Cette méthode doit être implémentée par toutes les sous-classes.

        Returns:
            str: Le son produit par l'animal.
        """
        pass


class Dog(Animal):
    """
    Classe représentant un chien.

    Hérite de la classe Animal et implémente la méthode sound()
    pour retourner le son caractéristique d'un chien.
    """

    def sound(self):
        """
        Retourne le son d'un chien.

        Returns:
            str: "Bark" - le son produit par un chien.
        """
        return "Bark"


class Cat(Animal):
    """
    Classe représentant un chat.

    Hérite de la classe Animal et implémente la méthode sound()
    pour retourner le son caractéristique d'un chat.
    """

    def sound(self):
        """
        Retourne le son d'un chat.

        Returns:
            str: "Meow" - le son produit par un chat.
        """
        return "Meow"
