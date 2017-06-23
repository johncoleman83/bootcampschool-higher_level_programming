#!/usr/bin/python3
from sys import argv


def nqueens(columns, rows):
    """begins nqueens adding new y digit for each x digit"""
    solutions = [[]]
    for x in range(columns):
        solutions = add_one_queen(x, rows, solutions)
    return solutions


def add_one_queen(x, rows, prev_solutions):
    """ adds one queen of y digit if it is safe for every solution """
    new_solutions = []
    for arrangement in prev_solutions:
        for y in range(rows):
            if y not in arrangement and is_safe(x, y, arrangement):
                new_solutions.append(arrangement + [y])
    return new_solutions


def is_safe(x, y, arrangement):
    """checks if queen is not on a diagonal"""
    return all(abs(arrangement[col] - y) != x - col
               for col in range(x))


def initiate_nqueens():
    """initiates nqueens checking for edge cases"""
    if len(argv) == 2:
        if argv[1].isdigit():
            n = int(argv[1])
        else:
            print('N must be a number')
            return(1)
        if n < 4:
            print('N must be at least 4')
            return(1)
        solutions = nqueens(n, n)
        for arrangement in solutions:
            formatted = []
            for x, y in enumerate(arrangement):
                formatted.append([x, y])
            print(formatted)
    else:
        print('Usage: nqueens N')


if __name__ == '__main__':
    initiate_nqueens()
