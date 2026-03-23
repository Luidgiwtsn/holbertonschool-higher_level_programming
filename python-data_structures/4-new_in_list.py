#!/usr/bin/python3
"""Module that contains the new_in_list function."""


def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position.

    Creates a copy of the original list and replaces the element
    at the specified index with a new element.

    Args:
        my_list: The original list.
        idx: The index position where the element should be replaced.
        element: The new element to insert at the specified index.

    Returns:
        A new list with the element replaced at the specified index.
        If idx is negative or out of range, returns a copy of the
        original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()

    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
