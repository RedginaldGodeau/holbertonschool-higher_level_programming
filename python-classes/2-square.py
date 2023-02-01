#!/usr/bin/python3
"""A Python Script"""


class Square:
    """
    Make a Square
    Args:
        __size (int): size.
    """

    def __init__(self, size):
        try:
            if (size < 0):
                raise ValueError
            elif (not isinstance(size, int)):
                raise TypeError
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
