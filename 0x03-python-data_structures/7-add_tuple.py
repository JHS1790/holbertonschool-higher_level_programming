#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if 1 <= len(tuple_a):
        a1 = tuple_a[0]
    else:
        a1 = 0
    if 2 <= len(tuple_a):
        a2 = tuple_a[1]
    else:
        a2 = 0
    if 1 <= len(tuple_b):
        b1 = tuple_b[0]
    else:
        b1 = 0
    if 2 <= len(tuple_b):
        b2 = tuple_b[1]
    else:
        b2 = 0
#    print("a1 = {} | a2 = {} | b1 = {} | b2 = {}".format(a1, a2, b1, b2))
    new_tuple = (a1 + b1, a2 + b2)
    return (new_tuple)
