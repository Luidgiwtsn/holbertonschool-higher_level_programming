#!/usr/bin/python3
"""Module pour les opérations de division sécurisées."""


def safe_print_division(a, b):
    """
    Divise deux entiers et affiche le résultat.

    Args:
        a: Le dividende (entier)
        b: Le diviseur (entier)

    Returns:
        Le résultat de la division en tant que flottant, ou None si la
        division échoue.

    Le résultat est affiché dans le bloc finally précédé de "Inside result:".
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
