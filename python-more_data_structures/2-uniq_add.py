#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(dict.fromkeys(my_list))
    n = 0

    for item in new_list:
        n += item

    return (n)
