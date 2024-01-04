#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lad = number % 10
if lad > 5:
    print(f"Last digit of {number:d} is {lad} and is greater than 5")
elif lad == 0:
    print(f"Last digit of {number:d} is {lad:d} and is 0")
elif lad < 6:
    print(f"Last digit of {number:d} is {lad:d} and is less than 6 and not 0")
