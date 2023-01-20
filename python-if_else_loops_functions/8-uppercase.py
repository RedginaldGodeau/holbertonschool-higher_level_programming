#!/usr/bin/python3
def uppercase(str):
    for x in str:
        character = x
        if "abcdefghijklmnopqrstwxyz".find(x) != -1:
            character = chr(ord(x) - 32)
        print("{character}".format(character = character), end = "")
    print("")
