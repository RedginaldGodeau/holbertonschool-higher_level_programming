#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    i = new.index(search)

    if i == -1:
        return (new)
    
    new[i] = replace
    return (new)
