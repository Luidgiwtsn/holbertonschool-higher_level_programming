#!/usr/bin/python3
"""Module to find the maximum integer in a list."""


def max_integer(my_list=[]):
    """Find and return the biggest integer in a list.

    Args:
        my_list: A list of integers. Defaults to an empty list.

    Returns:
        The maximum integer in the list, or None if the list is empty.
    """
    if not my_list:
        return None

    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value
