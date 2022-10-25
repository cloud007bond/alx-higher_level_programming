#!/usr/bin/python3
""" Module for task 1 """

def write_file(filename="", text=""):
    """ function for writting files """
    with open(filename, "w", enconding="utf-8") as f:
        return f.write(text)
