#!/usr/bin/env python3

# This program will display name and age 

import sys

if (len(sys.argv) != 3):
    print("Usage: ./lab2d.py name age")
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]

print('Hi ' + name + ', you are ' + str(age) + ' years old.')
