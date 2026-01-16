#!/usr/bin/python3
"""Module that imports and prints a variable from variable_load_5.py.

This module demonstrates how to import a specific variable from another
module and print its value. The code is protected by __name__ == "__main__"
to prevent execution when imported.
"""

if __name__ == "__main__":
    from variable_load_5 import a
    print("{}".format(a))
