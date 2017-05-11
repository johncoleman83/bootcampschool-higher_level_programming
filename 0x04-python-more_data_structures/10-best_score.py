#!/usr/bin/python3
def best_score(my_dict):
    if my_dict:
        return sorted(list([k, v] for k, v in my_dict.items()),
                      key=lambda x: x[1])[-1][0]
