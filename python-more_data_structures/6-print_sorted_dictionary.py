#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    Keys = list(a_dictionary.keys())
    Keys.sort()
    sorted_dict = {i: a_dictionary[i] for i in Keys}

    for item in sorted_dict:
        print(f"{item}: {sorted_dict[item]}")
