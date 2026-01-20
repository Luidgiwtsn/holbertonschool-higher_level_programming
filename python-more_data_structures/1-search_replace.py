#!/usr/bin/python3
"""Module that contains the search_replace function."""


def search_replace(my_list, search, replace):
    """Replace all occurrences of an element in a new list.

    Args:
        my_list: The initial list.
        search: The element to replace in the list.
        replace: The new element.

    Returns:
        A new list with all occurrences of search replaced by replace.
    """
    return [replace if element == search else element for element in my_list]
