#!/usr/bin/python3
def print_square(size):
    if isinstance(size, int):
        if size >= 0:
            for row in range(size):
                print('#' * size)
        else:
            raise ValueError('size must be >= 0')
    else:
        raise TypeError('size must be an integer')
