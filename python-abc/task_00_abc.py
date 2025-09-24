#!/usr/bin/env python3
"""
Defines an abstract Animal class and its subclasses
dog and cat. Implements the sound method to
return a specific sound.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Represents a dog, subclass of Animal.
    """

    def sound(self):
        """
        Returns the sound made by a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Represents a cat, subclass of Animal.
    """

    def sound(self):
        """
        Returns the sound made by a cat.
        """
        return "Meow"
