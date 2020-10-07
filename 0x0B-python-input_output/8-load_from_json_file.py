#!/usr/bin/python3
"""file"""
import json


def load_from_json_file(filename):
    """function"""
    with open(filename) as WorkingFile:
        return json.load(WorkingFile)
