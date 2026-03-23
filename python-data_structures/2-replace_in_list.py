#!/usr/bin/python3
"""Module that defines a function to replace an element in a list."""


def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position.

    Args:
        my_list: The list to modify
        idx: The index where to replace the element
        element: The new element to insert

    Returns:
        The modified list if idx is valid, otherwise the original list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
