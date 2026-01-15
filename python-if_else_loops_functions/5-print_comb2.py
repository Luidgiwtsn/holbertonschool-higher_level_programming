#!/usr/bin/python3
"""
Print numbers from 0 to 99 separated by ', '.
Numbers are printed in ascending order with two digits.
Only one loop and no extra variables are used.
"""

for i in range(100):
    if i != 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
