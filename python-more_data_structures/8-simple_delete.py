#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    dict = a_dictionary.copy()
    while key in dict:
        del dict[key]
    return dict
