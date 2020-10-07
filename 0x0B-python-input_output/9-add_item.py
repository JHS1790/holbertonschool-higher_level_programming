#!/usr/bin/python3
"""file"""
import sys
import os.path
from os import path
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

if path.exists("add_item.json"):
    NewList = load_from_json_file("add_item.json")
else:
    NewList = []
i = 1
while i < len(sys.argv):
    NewList.append(sys.argv[i])
    i += 1

save_to_json_file(NewList, "add_item.json")
