#!/usr/bin/python3
from sys import argv


def generate_board(n):
    board = []
    y = n - 1
    while (y >= 0):
        row = list([x, y] for x in range(n))
        board.append(row)
        y -= 1
    return board


def print_matrix(chess_array):
    for sub in chess_array:
        sub.sort(key = lambda row: row[0])
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


def init_queens(board):
    result = []
    n = len(board)
    startrow = 0
    start = 0
    while start < n:
        while startrow < n:
            positions = place_queens(n, board, start, startrow)
            if len(positions):
                for found in positions:
                    if found not in result:
                        copy = list(found)
                        result.append(copy)
            startrow += 1
        start += 1
    return result


def place_queens(n, board, start, startrow):
    s = start
    positions = []
    result = []
    while 1 == 1:
        del positions[:]
        switch = 1
        row = startrow
        while 1 == 1:
            start2 = s
            if switch:
                switch = 0
                if start2:
                    square = s
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
            if row == n:
                row = 0
            if row == startrow:
                break
        if len(positions) == n:
            copy = list(positions)
            result.append(copy)
        s += 1
        if s == n:
            s = 0
        if s == start:
            break
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
    print("the board")
    print_matrix(board)
    result = init_queens(board)
    print("\nthe solution")
    print_matrix(result)




if __name__ == '__main__':
    nqueens()
