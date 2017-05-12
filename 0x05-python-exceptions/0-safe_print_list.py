#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    l = len(my_list)
    for i in range(0, x if x < l else l):
        try:
            print("{}".format(my_list[i]), end='')
            count += 1
        except:
            break
    if count > 0:
        print()
    return count
