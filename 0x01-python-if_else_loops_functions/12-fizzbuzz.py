#!/usr/bin/python3
def fizzbuzz():
    s = ["{:d}", "Fizz", "Buzz", "FizzBuzz"]
    for i in range(1, 101):
        print(s[(i % 3 == 0) + 2 * (i % 5 == 0)].format(i), end=' ')
