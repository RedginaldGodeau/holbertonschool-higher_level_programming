#!/usr/bin/python3
""" Doc """

def text_indentation(text):
    """ Doc """

    if text == None or not isinstance(text, str):
        raise TypeError("text must be a string")

    spaceCheck = False
    for letter in text:
        if "?.:".find(letter) != -1:
            print(letter, end="")
            print("\n")
            spaceCheck = True
        else:
            if spaceCheck and letter == ' ':
                pass
            else:
                print(letter, end="")
                spaceCheck = False
