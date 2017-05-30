#!/usr/bin/python3
"""module to check if classes are the exact same class"""


def is_same_class(obj, a_class):
    """returns True if classes are the exact same class"""
    return(obj.__class__ == a_class)
