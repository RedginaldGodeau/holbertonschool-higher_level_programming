#!/usr/bin/python3
""" DOCUMENTATION """

import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


data = []

try:
    data = load_from_json_file("add_item.json")
    save_to_json_file(data + sys.argv[1:], "add_item.json")
except:
    save_to_json_file(sys.argv[1:], "add_item.json")