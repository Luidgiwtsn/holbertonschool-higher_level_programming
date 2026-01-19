#!/usr/bin/python3
"""Module that defines a function to retrieve an element from a list."""


def element_at(my_list, idx):
    """
    Retrieve an element from a list at a given index.

    Args:
        my_list: The list to retrieve the element from.
        idx: The index of the element to retrieve.

    Returns:
        The element at the given index, or None if the index is negative
        or out of range.
    """
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
