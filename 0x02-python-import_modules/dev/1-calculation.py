#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    sym = ['+', '-', '*', '/']
    op = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
    for i in range(0, 4):
        print('{:d} {:} {:d} = {:d}'.format(a, sym[i], b, op[i]))

if __name__ == "__main__":
    main()
