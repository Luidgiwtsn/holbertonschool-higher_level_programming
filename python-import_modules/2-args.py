#!/usr/bin/python3
"""Affiche le nombre et la liste des arguments passés au script."""


if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print(f"{argc} arguments:")

    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
