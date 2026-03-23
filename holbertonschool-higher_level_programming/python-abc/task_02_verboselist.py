#!/usr/bin/env python3
"""
Module définissant la classe VerboseList.

Ce module contient une classe VerboseList qui étend la classe list
intégrée de Python pour ajouter des notifications lors des modifications.
"""


class VerboseList(list):
    """
    Classe VerboseList qui étend la classe list intégrée.

    Cette classe imprime des messages de notification chaque fois qu'un
    élément est ajouté (via append ou extend) ou supprimé (via remove ou pop).
    """

    def append(self, item):
        """
        Ajoute un élément à la fin de la liste.

        Imprime un message de notification après l'ajout.

        Args:
            item: L'élément à ajouter à la liste.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Étend la liste en ajoutant tous les éléments de l'itérable.

        Imprime un message indiquant le nombre d'éléments ajoutés.

        Args:
            iterable: Un itérable contenant les éléments à ajouter.
        """
        items_to_add = list(iterable)
        count = len(items_to_add)
        super().extend(items_to_add)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Supprime la première occurrence d'un élément de la liste.

        Imprime un message de notification avant la suppression.

        Args:
            item: L'élément à supprimer de la liste.

        Raises:
            ValueError: Si l'élément n'est pas dans la liste.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Supprime et retourne un élément à l'index donné.

        Par défaut, supprime le dernier élément. Imprime un message
        de notification avant la suppression.

        Args:
            index (int, optional): L'index de l'élément à supprimer.
                                   Par défaut -1 (dernier élément).

        Returns:
            L'élément supprimé de la liste.

        Raises:
            IndexError: Si la liste est vide ou l'index est hors limites.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
