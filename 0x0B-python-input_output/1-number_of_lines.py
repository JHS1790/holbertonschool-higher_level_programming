#!/usr/bin/python3
"""file"""


def number_of_lines(filename=""):
    """function"""
    NoL = 0
    with open(filename, "r") as WorkingFile:
        for CurrentLine in WorkingFile:
            NoL += 1
    return NoL
