#!/usr/bin/env python3
"""
defines the Fish, Bird, and FlyingFish classes.
It demonstrates multiple inheritance and method overriding in Python.
"""


class Fish:
    """
    Represents a fish.
    """

    def swim(self):
        """
        Prints the swimming behavior of a fish.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints the habitat of a fish.
        """
        print("The fish lives in the water")


class Bird:
    """
    Represents a bird.
    """

    def fly(self):
        """
        Prints the flying behavior of a bird.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints the habitat of a bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish, inheriting from Fish and Bird.
    """

    def swim(self):
        """
        Prints the swimming behavior of a flying fish.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Prints the flying behavior of a flying fish.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Prints the habitat of a flying fish.
        """
        print("The flying fish lives both in water and the sky!")
