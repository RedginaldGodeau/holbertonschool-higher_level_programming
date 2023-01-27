#!/usr/bin/python3
def safe_print_division(a, b):
    r = None
    try:
        r = a / b 
        return (r)
    except:
        return (None)
    print("Inside result: {:d}".format(r))
