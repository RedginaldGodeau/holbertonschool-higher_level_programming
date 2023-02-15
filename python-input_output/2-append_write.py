#!/usr/bin/python3
""" DOCUMENTATION """


def append_write(filename="", text=""):
    """ FUNCTION """
    with open(filename, "a", encoding="utf-8") as f:
        print(f.write(text))
