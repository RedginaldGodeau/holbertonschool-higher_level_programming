#!/usr/bin/python3
""" DOCUMENTATION """


def write_file(filename="", text=""):
    """ FUNCTION """
    with open(filename, "w", encoding="utf-8") as f:
        print(f.write(text), end="")