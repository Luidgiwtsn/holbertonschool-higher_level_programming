#!/usr/bin/python3
"""Module that defines a function to update a dictionary."""


def update_dictionary(a_dictionary, key, value):
    """Update or add a key/value pair in a dictionary.

    Args:
        a_dictionary: The dictionary to update
        key: The key to update or add
        value: The value to assign to the key

    Returns:
        The updated dictionary (same object as a_dictionary)
    """
    a_dictionary[key] = value
    return a_dictionary
