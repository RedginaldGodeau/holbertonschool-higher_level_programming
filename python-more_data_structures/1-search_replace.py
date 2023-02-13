#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = my_list.find(search)

    if i == -1:
        return (my_list)

    new = my_list.copy()
    new[i] = replace

    return (new)
