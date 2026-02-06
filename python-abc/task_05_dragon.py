#!/usr/bin/env python3
"""
Module définissant les mixins SwimMixin et FlyMixin ainsi que la classe Dragon.

Ce module illustre l'utilisation des mixins pour ajouter des capacités
multiples à une classe via l'héritage multiple.
"""


class SwimMixin:
    """
    Mixin qui ajoute la capacité de nager à une classe.

    Ce mixin fournit une méthode swim() qui peut être utilisée
    par toute classe héritant de ce mixin.
    """

    def swim(self):
        """
        Permet à la créature de nager.

        Affiche un message indiquant que la créature nage.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin qui ajoute la capacité de voler à une classe.

    Ce mixin fournit une méthode fly() qui peut être utilisée
    par toute classe héritant de ce mixin.
    """

    def fly(self):
        """
        Permet à la créature de voler.

        Affiche un message indiquant que la créature vole.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Classe représentant un dragon.

    Cette classe hérite de SwimMixin et FlyMixin, ce qui lui confère
    les capacités de nager et de voler. Elle possède également sa propre
    méthode roar() pour rugir.
    """

    def roar(self):
        """
        Permet au dragon de rugir.

        Affiche un message indiquant que le dragon rugit.
        """
        print("The dragon roars!")
