#!/usr/bin/python3
for x in range(1,99):
    if x % 3 == 0:
        print("Fizz", end="")
    if x % 5 == 0:
        print("Buzz", end="")
    if x % 3 != 00 and x % 5 != 0:
        print(x, end="")
    print(" ", end="")
