#!/usr/bin/python3
"""file"""
import json


def save_to_json_file(my_obj, filename):
    """function"""
    with open(filename, mode="w") as WorkingFile:
        json.dump(my_obj, WorkingFile)
