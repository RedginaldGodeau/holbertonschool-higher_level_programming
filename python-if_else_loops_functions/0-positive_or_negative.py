#!/usr/bin/python3
import random

number = random.randint

if number > 0 :
    print(f"{number} is positive\n")
elif number == 0 :
    print(f"{number} is zero\n")
elif number < 0 :
    print(f"{number} is negative\n")