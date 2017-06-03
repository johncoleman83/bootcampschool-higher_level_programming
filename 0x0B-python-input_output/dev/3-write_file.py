#!/usr/bin/python3
def write_file(filename="", text=""):
    """writes string to file"""
    chars_written = 0
    with open(filename, mode='w', encoding='utf-8') as f_io:
        chars_written += f_io.write(text)
        f_io.close()
    return chars_written
