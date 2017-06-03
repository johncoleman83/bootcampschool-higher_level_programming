#!/usr/bin/python3
def class_to_json(obj):
    """returns dict representation of class"""
    try:
        obj_dict = obj.__dict__
        return obj_dict
    except:
        return {}
