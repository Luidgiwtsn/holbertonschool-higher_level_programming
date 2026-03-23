#!/usr/bin/python3
"""
Module that imports the add function and performs addition.

This module demonstrates importing a function from another module
and using it to add two numbers together.
"""

if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
