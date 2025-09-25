#!/usr/bin/env python3
"""
Contains mixins and a
Dragon class demonstrating multiple inheritance.
"""


class SwimMixin:
    """
    Mixin class that provides swimming ability.
    """

    def swim(self):
        """
        Print a message indicating the creature can swim.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying ability.
    """

    def fly(self):
        """
        Print a message indicating the creature can fly.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon, which can swim, fly, and roar.
    """
    def roar(self):
        """
        Print a message indicating the dragon is roaring.
        """
        print("The dragon roars!")
