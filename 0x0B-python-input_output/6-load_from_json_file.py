#!/usr/bin/python3
"""
Module 8-load_from_json_file
Contains functions that creates a python obj from JSON file
"""


def load_from_json_file(filename):
    """Creates a python objfrom JSON file
    Args:
        filename: file
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
