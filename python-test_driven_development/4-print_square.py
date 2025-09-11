#!/usr/bin/python3
def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): The size length of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
