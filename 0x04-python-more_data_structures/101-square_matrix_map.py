#!/usr/bin/python3
def square_matrix_map(m=[]):
    return list(map(lambda i: list(map(lambda y: y**2, m[i])), range(len(m))))
