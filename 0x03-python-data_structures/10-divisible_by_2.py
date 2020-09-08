#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    even_list = []
    for x in range(0, len(my_list), 1):
        if my_list[x] == 0:
            even_list.append(True)
        elif my_list[x] % 2 == 0:
            even_list.append(True)
        else:
            even_list.append(False)
    return (even_list)
