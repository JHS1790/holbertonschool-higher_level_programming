#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    max_int = my_list[0]
    for x in range(0, len(my_list), 1):
        if my_list[x] > max_int:
            max_int = my_list[x]
    return (max_int)
