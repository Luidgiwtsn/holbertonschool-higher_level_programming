#!/usr/bin/python3
"""
This script prints numbers from 00 to 99, separated by ', '.
Numbers are printed in ascending order with two digits.
The last number is followed by a newline.
"""

for i in range(100):
    if i < 99:
        print("%02d, " % i, end="")
    else:
        print("%02d" % i)
