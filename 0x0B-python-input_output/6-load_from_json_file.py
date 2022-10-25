#!/usr/bin/python3
""" module for task 6 """
import json

def load_from_json_file(filename):
    """ function that loads json to file """
    with open(filename,"r")as f:
        return json.load(f)

