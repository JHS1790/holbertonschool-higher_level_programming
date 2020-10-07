#!/usr/bin/python3
"""file"""


def read_file(filename=""):
    """function"""
    with open(filename, "r") as WorkingFile:
        for CurrentLine in WorkingFile:
            print(CurrentLine, end="")
