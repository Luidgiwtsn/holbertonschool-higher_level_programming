#!/usr/bin/python3
"""
Module qui affiche les nombres de 1 à 100 avec les règles FizzBuzz :
- Les multiples de 3 sont remplacés par "Fizz"
- Les multiples de 5 sont remplacés par "Buzz"
- Les multiples de 3 et 5 sont remplacés par "FizzBuzz"
Chaque élément est suivi d'un espace.
"""


def fizzbuzz():
    """Affiche les nombres de 1 à 100 en appliquant
    les substitutions FizzBuzz."""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
