#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """reads N lines from file or entire file"""
    if nb_lines < 0:
        nb_lines = 0
    with open(filename, mode='r', encoding='utf-8') as a_file:
        for i, line in enumerate(a_file):
            if (nb_lines and nb_lines == i):
                break
            print(line, end='')
        a_file.close()
