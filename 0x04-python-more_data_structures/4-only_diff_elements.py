#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_set_1 = {x for x in set_1 if x not in set_2}
    unique_set_2 = {x for x in set_2 if x not in set_1}
    return unique_set_1.union(unique_set_2)
