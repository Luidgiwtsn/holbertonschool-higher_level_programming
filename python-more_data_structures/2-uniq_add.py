#!/usr/bin/python3
"""Module that adds all unique integers in a list."""


def uniq_add(my_list=[]):
    """Add all unique integers in a list.

    Args:
        my_list: A list of integers (may contain duplicates).

    Returns:
        The sum of all unique integers in the list.
    """
    unique_integers = set(my_list)
    return sum(unique_integers)
