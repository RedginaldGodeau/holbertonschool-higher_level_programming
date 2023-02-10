#!/usr/bin/python3
""" DOCUMENTATION """

import json

def load_from_json_file(filename):
    """ FUNCTION """
    
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f.read())
        f.close()
        return (data)
    
