#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_student = ''
    best_score = 0
    for key in a_dictionary:
        if a_dictionary[key] >= best_score:
            best_student = key
            best_score = a_dictionary[key]
    return best_student
