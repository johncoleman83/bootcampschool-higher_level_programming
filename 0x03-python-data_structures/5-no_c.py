#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        my_string = [l for l in my_string if l.lower() != 'c']
        my_string = ''.join(my_string)
    return (my_string)
