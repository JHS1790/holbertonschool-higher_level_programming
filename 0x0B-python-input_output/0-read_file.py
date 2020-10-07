#!/usr/bin/python3
"""file"""


def read_file(filename=""):
    """function"""
    with open(filename, "r", encoding="UTF8") as WorkingFile:
        for CurrentLine in WorkingFile:
            print(CurrentLine, end="")
