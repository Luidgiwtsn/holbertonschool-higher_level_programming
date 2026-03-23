#!/usr/bin/python3
"""Module pour les opérations de division de listes."""


def list_division(my_list_1, my_list_2, list_length):
    """
    Divise les éléments de deux listes élément par élément.

    Args:
        my_list_1: Première liste contenant tout type d'éléments
        my_list_2: Deuxième liste contenant tout type d'éléments
        list_length: Longueur de la liste résultat

    Returns:
        Une nouvelle liste de longueur list_length avec les résultats
        des divisions. Retourne 0 pour les éléments qui ne peuvent
        pas être divisés.

    Affiche des messages d'erreur pour:
        - "wrong type": quand l'élément n'est pas int ou float
        - "division by 0": lors d'une division par zéro
        - "out of range": quand l'index de la liste est hors limites
    """
    result = []

    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
            result.append(division)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass

    return result
