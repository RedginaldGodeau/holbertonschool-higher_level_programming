#!/usr/bin/python3
""" Doc """

def add_integer(a, b=98):
     """ Doc """
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    else:
        return (int) (a + b)

