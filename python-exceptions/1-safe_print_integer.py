#!/usr/bin/python3
"""Module that defines a function to safely print integers."""


def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value: The value to print (can be any type).

    Returns:
        True if value has been correctly printed (value is an integer).
        False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
