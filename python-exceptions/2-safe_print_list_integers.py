#!/usr/bin/python3
"""Module qui définit la fonction safe_print_list_integers."""


def safe_print_list_integers(my_list=[], x=0):
    """Affiche les x premiers entiers d'une liste.

    Args:
        my_list: Une liste pouvant contenir n'importe quel type d'éléments.
        x: Le nombre d'éléments à accéder dans my_list.

    Returns:
        Le nombre réel d'entiers affichés.

    Raises:
        IndexError: Si x est plus grand que la longueur de my_list.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
