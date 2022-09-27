#!/usr/bin/python3
"""
Module 7-save_to_json_file
Contains function that writes python obj to file using JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Writes python obj to file using JSON representation
    Args:
        my_obj: python object
        filename: file
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
