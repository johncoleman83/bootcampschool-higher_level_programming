#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for c in ['.', '?', ':']:
        text = text.replace(c, c + '\n\n')
    new = []
    for line in text.split('\n'):
        new.append(line.strip(' '))
    print('\n'.join(new), end='')
