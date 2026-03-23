#!/usr/bin/python3
"""
Print all numbers from 0 to 98 in decimal and hexadecimal.
Each line displays the decimal and hexadecimal representation.
"""

for i in range(0, 99):
    print("{} = {}".format(i, hex(i)))
