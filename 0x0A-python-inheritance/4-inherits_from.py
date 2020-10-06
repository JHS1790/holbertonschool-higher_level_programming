#!/usr/bin/python3
"""a file"""


def inherits_from(obj, a_class):
    """a func"""
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
