#!/usr/bin/python3
""" Module for task 2 """

def append_write(filename="", text=""):
    """ function for writing filrs """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
