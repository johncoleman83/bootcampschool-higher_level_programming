#!/usr/bin/python3
from sys import argv


def nqueens(columns, rows):
    solutions = [[]]
    for x in range(columns):
        solutions = add_one_queen(x, rows, solutions)
    print(solutions)
    return solutions


def add_one_queen(x, rows, prev_solutions):
    print("add_one_queen() rows={}, x = {}, prev_sols\n{}".format(rows, x, prev_solutions))
    new_solutions = []
    for arrangement in prev_solutions:
        for y in range(rows):
            if is_safe(x, y, arrangement):
                new_solutions.append(arrangement + [y])
    return new_solutions


def is_safe(x, y, arrangement):
    print("is_safe() x: {}, y: {}, arrangement: {}".format(x, y, arrangement))
    return all(arrangement[col] != y and
               abs(arrangement[col] - y) != x - col
               for col in range(x))

def initiate_nqueens():
    if len(argv) > 1:
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
        print('N must be at least 4')


if __name__ == '__main__':
    initiate_nqueens()
