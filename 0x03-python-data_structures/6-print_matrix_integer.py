#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix:
        i = 0
        while i < len(matrix):
            j = 0
            if matrix[i]:
                l = len(matrix[i])
                while j < l:
                    print("{:d}{:}".format(matrix[i][j],
                                           (' ' if j < l - 1
                                            else '\n')), end="")
                    j += 1
            else:
                print(matrix[i])
            i += 1
