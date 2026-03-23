#!/usr/bin/python3
"""Module for tuple addition."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples element-wise.

    Args:
        tuple_a: First tuple (default: empty tuple)
        tuple_b: Second tuple (default: empty tuple)

    Returns:
        A tuple with 2 integers representing the sum of corresponding elements.
        Missing elements are treated as 0.
        Extra elements beyond the first 2 are ignored.
    """
    # Extract first elements, default to 0 if missing
    a0 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a1 = tuple_a[1] if len(tuple_a) >= 2 else 0

    # Extract second elements, default to 0 if missing
    b0 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b1 = tuple_b[1] if len(tuple_b) >= 2 else 0

    # Return tuple with sums
    return (a0 + b0, a1 + b1)
