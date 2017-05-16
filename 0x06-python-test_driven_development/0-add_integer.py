#!/usr/bin/python3
"""
module with 1 function, add integers
"""


def add_integer(a, b):
    """returns a + b"""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return int(a) + int(b)
    else:
        raise TypeError("{:} must be an integer"
                        .format('b' if isinstance(a, (int, float)) else 'a'))
