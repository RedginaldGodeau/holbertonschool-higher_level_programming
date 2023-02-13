#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

def update_dictionary(a_dictionary, key, value):

    new_key = {key: value}

    if key in a_dictionary:
        a_dictionary.update(new_key)
    else:
        a_dictionary[key] = value;
    return a_dictionary
