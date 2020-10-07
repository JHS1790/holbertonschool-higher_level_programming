#!/usr/bin/python3
"""file"""


def append_write(filename="", text=""):
    """function"""
    with open(filename, mode="a", encoding="UTF8") as WorkingFile:
        return WorkingFile.write(text)
