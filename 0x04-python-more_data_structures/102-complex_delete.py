#!/usr/bin/python3
def complex_delete(my_dict, value):
    new = {k: v for k, v in my_dict.items() if v == value}
    for key in new:
        my_dict.pop(key)
    return my_dict
