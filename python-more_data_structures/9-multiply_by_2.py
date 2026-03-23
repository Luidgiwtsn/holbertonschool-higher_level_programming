#!/usr/bin/python3
"""Module that defines a function to multiply dictionary values by 2."""


def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary: A dictionary with integer values

    Returns:
        A new dictionary with all values multiplied by 2
    """
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
