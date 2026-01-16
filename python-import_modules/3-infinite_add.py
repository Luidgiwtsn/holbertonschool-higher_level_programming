#!/usr/bin/python3
"""Module qui additionne tous les arguments de ligne de commande.

Ce module fournit une fonctionnalité pour additionner un nombre
illimité d'arguments entiers passés via la ligne de commande et
afficher le résultat.
"""


def add_arguments():
    """Additionne tous les arguments de ligne de commande et affiche le résultat.

    Cette fonction récupère tous les arguments de ligne de commande (excluant
    le nom du script), les convertit en entiers, les additionne, et affiche
    la somme suivie d'une nouvelle ligne.

    Returns:
        None
    """
    import sys

    total = 0
    for arg in sys.argv[1:]:
        total += int(arg)
    print(total)


if __name__ == "__main__":
    add_arguments()
