#!/usr/bin/python3
"""
Print the ASCII alphabet in lowercase, excluding 'q' and 'e',
without a trailing newline.converts an ASCII value to its
corresponding character.
"""

for i in range(97, 123):
    if i != 101 and i != 113:
        print("{:c}".format(i), end="")
