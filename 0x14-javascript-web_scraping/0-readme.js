#!/usr/bin/node
import sys

try:
    file_path = sys.argv[1]
    with open(file_path, "r", encoding="utf-8") as file:
        print(file.read())
except Exception as e:
    print(e)
