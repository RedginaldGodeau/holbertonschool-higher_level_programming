#!/usr/bin/python3
""" DOCUMENTATION """


def write_file(filename="", text=""):
    """ FUNCTION """

   f = open(filename, "w")
   print(f.write(text))
