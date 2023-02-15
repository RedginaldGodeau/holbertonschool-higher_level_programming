#!/usr/bin/python3
""" DOCUMENTATION """


def read_file(filename=""):
    """ FUNCTION """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
