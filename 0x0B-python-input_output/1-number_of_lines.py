#!/usr/bin/python3
def number_of_lines(filename=""):
    """returns number of lines in a file"""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        for i, l in enumerate(a_file):
            pass
    return i + 1
