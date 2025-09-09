#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for key in sorted(a_dictionary):
        del a_dictionary[key]
        return a_dictionary
