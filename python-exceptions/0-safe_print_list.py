#!/usr/bin/python3
"""Print x elements of a list."""


def safe_print_list(my_list=[], x=0):

    """Args:
        my_list: A list containing elements of any type.
        x: The number of elements to print.

    Returns:
        The actual number of elements printed.
    """

    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
