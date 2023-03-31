#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dict = a_dictionary.copy()
    for key, value in dict.items():
        dict[key] *= 2
    return dict
