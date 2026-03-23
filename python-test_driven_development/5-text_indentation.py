#!/usr/bin/python3
"""Module pour l'indentation de texte."""


def text_indentation(text):
    """Affiche un texte avec 2 nouvelles lignes après '.', '?' et ':'.

    Args:
        text: La chaîne de caractères à formater et afficher.

    Raises:
        TypeError: Si text n'est pas une chaîne de caractères.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
