#!/usr/bin/python3
"""Module that defines a function to print a dictionary with sorted keys."""


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary with keys in alphabetical order.

    Args:
        a_dictionary: A dictionary with string keys to be printed.

    Only the first level keys are sorted. Dictionary values can be of any type.
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
