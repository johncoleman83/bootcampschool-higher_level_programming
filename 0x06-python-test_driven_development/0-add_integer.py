#!/usr/bin/python3
def add_integer(a, b):
    try:
        if a == int(a) or a == float(a):
            a = int(a)
            try:
                if b == int(b) or b == float(b):
                    b = int(b)
            except:
                raise TypeError("b must be an integer")
    except:
        raise TypeError("a must be an integer")
    return a + b
