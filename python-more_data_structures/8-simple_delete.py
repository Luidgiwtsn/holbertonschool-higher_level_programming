#!/usr/bin/python3
"""Module that defines a function to delete a key in a dictionary."""


def simple_delete(a_dictionary, key=""):
    """
    Delete a key in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to modify
        key (str): The key to delete. Defaults to empty string.

    Returns:
        dict: The modified dictionary (same object as input)

    Note:
        If the key doesn't exist, the dictionary is not modified.
        The function modifies the original dictionary and returns it.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
