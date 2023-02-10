#!/usr/bin/python3
""" DOCUMENTATION """

import json

def save_to_json_file(my_obj, filename):
    """ FUNCTION """

    with open(filename, "a", encoding="utf-8") as f:
       f.write(json.dumps(my_obj))
