#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum, items = 0, 0
        for x, y in my_list:
            sum += x * y
            items += y
        return sum / items
    return 0
