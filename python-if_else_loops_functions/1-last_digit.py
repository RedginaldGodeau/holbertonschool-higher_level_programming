#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10 if number > 0 else ((number * -1) % 10) * -1
if number > 5:
    print(f"Last digit of {number} is {lastdigit}\
 and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {lastdigit}\
 and is 0")
elif number < 6:
    print(f"Last digit of {number} is {lastdigit}\
 and is less than 6 and not 0")
