#!/usr/bin/env python3
"""
provides a CountedIterator class that wraps around an iterable
and tracks the number of elements that have been iterated.
"""


class CountedIterator:
    """
    An iterator that counts how many items have been iterated over.

    Attributes:
        iterator (iterator): The wrapped iterator.
        count (int): Number of items that have been returned so far.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            iterable (iterable): Any iterable object.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.

        Raises:
            StopIteration: When there are no more items to iterate.

        Returns:
            The next item from the original iterable.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Get the number of items returned so far.

        Returns:
            int: The number of items iterated.
        """
        return self.count
