#!/usr/bin/python3
from sys import argv


def generate_board(n):
    board = []
    y = n - 1
    while (y >= 0):
        row = list([x, y] for x in range(4))
        board.append(row)
        y -= 1
    return board


def print_matrix(chess_array):
    for sub in chess_array:
        print(sub)


def is_safe(positions, square):
    for s in positions:
        if s[0] == square[0]:
            return False
        if s[1] == square[1]:
            return False
        if abs(s[0] - square[0]) == abs(s[1] - square[1]):
            return False
    return True


def place_queens(board):
    result = []
    positions = []
    n = len(board)
    start = 0
    while start < n:
        del positions[:]
        switch = 1
        row = 0
        while row < n:
            start2 = start
            if switch:
                switch = 0
                if start2:
                    square = start
                    start2 = 0
                else:
                    square = 0
                while (square < n):
                    if is_safe(positions, board[row][square]):
                        positions.append(board[row][square])
                    square += 1
            else:
                switch = 1
                square = n - 1
                while (square >= 0):
                    if is_safe(positions, board[row][square]):
                        positions.append(board[row][square])
                    square -= 1
            row += 1
        if len(positions) == n:
            copy = list(positions)
            result.append(copy)
        start += 1
    return result


def nqueens():
    if argv[1].isdigit():
        n = int(argv[1])
    else:
        print('N must be a number')
        return(1)
    if n < 4:
        print('N must be at least 4')
        return(1)
    board = generate_board(n)
    result = place_queens(board)
    print(result)





if __name__ == '__main__':
    nqueens()
