#!/usr/bin/env python3
"""
Defines the Verboselist class a subclass of list that provides
verbose output for list modification methods.
"""


class VerboseList(list):
    """
    A subclass of list that prints messages whenever the list is modified
    using append, extend, remove, or pop methods.
    """

    def append(self, item):
        """
        Append item to the list and print a confirmation message.
        """
        super().append(item)
        print(f"Added[{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with elements from the iterable and print a message
        indicating how many items were added.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Extend the list with elements from the iterable and print a message
        indicating how many items were added.
        """
        print(f"Remove[{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return item at index (default last).
        Print the popped item before removing it.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
