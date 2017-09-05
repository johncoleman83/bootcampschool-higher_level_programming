#!/usr/bin/python3
import sys


def nqueens(columns, rows):
    """begins nqueens adding new y digit for each x digit"""
    solutions = [[]]
    for x in range(columns):
        solutions = add_queens(x, rows, solutions)
    return solutions


def add_queens(x, rows, prev_solutions):
    """ adds one queen of y digit if it is safe for every solution """
    new_solutions = []
    for arrangement in prev_solutions:
        for y in range(rows):
            if is_safe(x, y, arrangement):
                new_solutions.append(arrangement + [y])
    return new_solutions


def is_safe(x, y, arrangement):
    """checks if queen is unique and not on a diagonal"""
    if y in arrangement:
        return (False)
    else:
        return all(abs(arrangement[col] - y) != x - col
                   for col in range(x))


def check_edge_cases():
    """checks edge based on nqueens input"""
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)
    return(n)


def initiate_nqueens():
    """initiates nqueens checking for edge cases, then builds chess board"""
    n = check_edge_cases()
    solutions = nqueens(n, n)
    for arrangement in solutions:
        formatted = []
        for x, y in enumerate(arrangement):
            formatted.append([x, y])
        print(formatted)

if __name__ == '__main__':
    """MAIN APP"""
    initiate_nqueens()
