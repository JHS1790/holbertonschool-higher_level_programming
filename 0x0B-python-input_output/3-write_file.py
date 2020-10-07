#!/usr/bin/python3
"""File"""


def write_file(filename="", text=""):
    """function"""
    with open(filename, "w", encoding="UTF-8") as WorkingFile:
        return WorkingFile.write(text)
