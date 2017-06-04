#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """appends new string after every line containing substring"""
    with open(filename, mode='r', encoding='utf-8') as f_io:
        f_lines = f_io.readlines()
        f_io.close()
    i = 0
    while i < len(f_lines):
        if search_string in f_lines[i]:
            f_lines.insert(i + 1, new_string)
            i += 1
        i += 1
    f_lines = ''.join(f_lines)
    with open(filename, mode='w', encoding='utf-8') as f_io:
        f_io.write(f_lines)
        f_io.close()
