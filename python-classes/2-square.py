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
                raise ValueInf
            self.__size = size
        except ValueInf:
            print("size must be >= 0")
        except ValueError:
            print("Could not convert data to an integer.")
