#!/usr/bin/python3

def roman_to_int(roman_string):
    numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    result = 0
    save_result = 0

    for i in range(len(roman_string) - 1):
        letters = (numbers.get(roman_string[i], 0), numbers.get(
            roman_string[i + 1], 0))
        save_result += letters[0]

        if letters[0] > letters[1]:
            result += save_result
            save_result = 0
        elif letters[0] < letters[1]:
            result -= save_result
            save_result = 0

    return result + save_result + numbers.get(roman_string[-1], 0)
