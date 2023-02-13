#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    remove_key = a_dictionary.pop(key, None)
    
    if remove_key != None:
        return remove_key
    else:
        return a_dictionary
