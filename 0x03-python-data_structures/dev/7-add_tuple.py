#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    for n in range(2):
        try:
            if tuple_a[n]:
                a[n] += tuple_a[n]
            if tuple_b[n]:
                a[n] += tuple_b[n]
        except:
            pass
    return a
