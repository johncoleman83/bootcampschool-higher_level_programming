#!/usr/bin/python3
def class_to_json(obj):
    """returns dict representation of class"""
    try:
        o_D = obj.__dict__
        D = dict([k, v] for k, v in o_D.items())
        return D
    except:
        return {}
