#!/usr/bin/python3
def multiply_by_2(my_dict):
    adict = {}
    for key in my_dict:
        adict[key] = my_dict[key] * 2
    return adict
