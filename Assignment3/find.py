#!/usr/bin/env python

import sys, os

def find_all(find_string, dir_path):
    """ Searches for files that contains "find_string" recursively from dir_path"""
    print("inne i find_all")
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            fullpath = os.path.join(root, f)
            if find_string in f:
                print(fullpath)

try:
    find_string = sys.argv[1]
    directory = sys.argv[2]
    print("== Searching for \"{0}\" within \"{1}\" ==".format(find_string, directory))
except:
    print("ERROR: Please enter a string and directory.")

find_all(find_string, directory)
