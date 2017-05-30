#!/usr/bin/python3
"""module to check classes of objects"""


def inherits_from(obj, a_class):
    """returns True if object is subclass of input class"""
    return (isinstance(obj, a_class) and (type(obj) != a_class))
