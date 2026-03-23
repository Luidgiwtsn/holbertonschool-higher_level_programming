#!/usr/bin/python3
"""Module that defines a function to return string
length and first character."""


def multiple_returns(sentence):
    """
    Return a tuple with the length of a string and its first character.

    Args:
        sentence (str): The input string to analyze.

    Returns:
        tuple: A tuple containing (length, first_character).
               If the sentence is empty, first_character is None.
    """
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return (length, first_char)
