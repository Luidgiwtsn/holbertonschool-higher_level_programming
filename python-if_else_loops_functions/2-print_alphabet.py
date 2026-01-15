#!/usr/bin/python3
"""
Prints the ASCII alphabet in lowercase without a trailing newline.
"""

print("{}".format("".join(chr(i) for i in range(97, 123))), end="")
