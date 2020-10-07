#!/usr/bin/python3
"""file"""


def read_lines(filename="", nb_lines=0):
    """function"""
    CurrentLineNumber = 0
    with open(filename, "r", encoding="UTF8") as WorkingFile:
        for CurrentLine in WorkingFile:
            CurrentLineNumber += 1
            if CurrentLineNumber <= nb_lines or nb_lines <= 0:
                print(CurrentLine, end="")
