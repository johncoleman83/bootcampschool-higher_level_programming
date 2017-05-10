#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        i = 0
        while len(my_string) > 0:
            l = len(my_string)
            if my_string[i] == 'c' or my_string[i] == 'C':
                if i == 0:
                    if i < l - 1:
                        my_string = my_string[1:]
                    else:
                        my_string = ""
                elif i == l - 1:
                    my_string = my_string[:l - 1]
                    break
                else:
                    my_string = my_string[:i] + my_string[i + 1:]
            i += 1
            if i >= len(my_string):
                break
    return my_string
