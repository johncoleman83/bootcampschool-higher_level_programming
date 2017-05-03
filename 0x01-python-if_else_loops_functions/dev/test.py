#!/usr/bin/python3
for x in range(1, 101):
    if x % 3 != 0 and x % 5 != 0:
        print(x, "", end="")
    if x % 5 == 0 and x % 3 == 0:
        print("FizzBuzz ", end="")
    elif x % 3 == 0:
        print("Fizz ", end="")
    elif x % 5 == 0:
        print("Buzz ", end="")
