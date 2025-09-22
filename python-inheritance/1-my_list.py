#!/usr/bin/python3
"""
defines the MyList class, which extends the built-in list
and provides an additional method to print the
list sorted without modifying it.
"""


class MyList(list):
    """
    MyList class that extends the built-in list.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order without
        modifying the original list.
        """
        print(sorted(self))
