#!/usr/bin/python3
globvar = 0
def magic_string():
    global globvar++
    return ("Holberton" * globvar)
