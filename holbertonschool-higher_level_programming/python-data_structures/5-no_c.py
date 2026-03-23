#!/usr/bin/python3
"""Module that removes all 'c' and 'C' characters from a string."""


def no_c(my_string):
    """Remove all occurrences of 'c' and 'C' from a string.

    Args:
        my_string: The input string to process.

    Returns:
        A new string with all 'c' and 'C' characters removed.
    """
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
