#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for c in ['.', '?', ':']:
        text = text.replace(c, c + '\n\n')
    new = [line.strip(' ') for line in text.split('\n')]
    print('\n'.join(new), end='')
