#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()

    while search in new:
        i = new.index(search)
        new[i] = replace

    return (new)
