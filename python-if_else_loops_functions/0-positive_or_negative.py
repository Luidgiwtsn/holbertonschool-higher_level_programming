#!/usr/bin/python3
"""
This program assigns a random signed number to a variable
and prints whether the number is positive, negative, or zero.
"""

import random

number = random.randint(-10, 10)

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
