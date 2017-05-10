#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    tup = (tuple_a, tuple_b)
    for i in range(2):
        if len(tup[0]) > i:
            a[i] += tup[0][i]
        if len(tup[1]) > i:
            a[i] += tup[1][i]
    return (a[0], a[1])
