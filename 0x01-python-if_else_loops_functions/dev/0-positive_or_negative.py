#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    print("{:d}".format(number), "is zero")
else:
    print(number, "is positive" if number > 0 else "is negative")