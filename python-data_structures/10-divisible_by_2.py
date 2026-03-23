#!/usr/bin/python3
"""Module that checks if numbers are divisible by 2."""


def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list.

    Args:
        my_list: A list of integers to check.

    Returns:
        A new list with True or False values indicating whether
        each integer at the same position is divisible by 2.
    """
    return [num % 2 == 0 for num in my_list]
