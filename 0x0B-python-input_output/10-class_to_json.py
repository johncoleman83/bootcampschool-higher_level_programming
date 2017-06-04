#!/usr/bin/python3
def class_to_json(obj):
    """returns dict representation of class"""
    try:
        o_D = (obj.__dict__)
        return o_D
    except:
        return {}
