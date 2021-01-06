#!/usr/bin/python3
"""6. Find a peak"""

def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers."""
    if list_of_integers:
        for x in range(len(list_of_integers)):
            if list_of_integers[x] > n:
                n = list_of_integers[x]
        return n
    return None
