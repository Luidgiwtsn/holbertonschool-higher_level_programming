#!/usr/bin/python3
"""
Prints the last digit of a randomly generated signed number
and describes its value.
"""

import random

number = random.randint(-10000, 10000)

# Get the last digit (keeping the sign)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit

# Print according to the rules
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(
        f"Last digit of {number} is {last_digit} "
        "and is less than 6 and not 0"
    )
