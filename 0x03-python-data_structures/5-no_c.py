#!/usr/bin/python3
def no_c(my_string):
    my_list = []
    for x in range(0, len(my_string)):
        if my_string[x] is not "C" and my_string[x] is not "c":
            my_list.append(my_string[x])
    return ("".join(my_list))
