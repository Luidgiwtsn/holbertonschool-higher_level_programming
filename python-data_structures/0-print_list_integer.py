#!/usr/bin/python3
"""Module for printing list integers."""


def print_list_integer(my_list=[]):
    """Print all integers of a list.

    Args:
        my_list: A list of integers (default: empty list).

    Returns:
        None
    """
    for number in my_list:
        print("{:d}".format(number))
