#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if not my_list or x == 0:
            print()
            return (0)

        for item in my_list:
            print(f"{item}", end="")
        print()
        return (my_list[x])
    except:
        return (my_list[-1])
