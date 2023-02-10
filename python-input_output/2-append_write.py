#!/usr/bin/python3
""" DOCUMENTATION """


def append_write(filename="", text=""):
    """ FUNCTION """

   f = open(filename, "a")
   print(f.write(text))
