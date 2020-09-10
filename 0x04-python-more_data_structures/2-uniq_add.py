#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)
    new_list = list(new_set)
    result = 0
    for x in range(len(new_list)):
        result += new_list[x]
    return result
