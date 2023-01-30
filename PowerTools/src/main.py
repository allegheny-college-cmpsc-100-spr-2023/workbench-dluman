#!/usr/bin/python

"""
Basic power/root calcuation program to demonstrate:

* functions
* arguments
  * defaults
* parameters

This program serves as part of the Allegheny College CMPSC 100: Computational
Expression course.
"""

# Necessary imports
import math
import suffix

# TODO: Write function to calculate result of various numbers 
#       raised to various powers.

# TODO: Write function to calculates nth root of a number 
#       by raising to fractional power

# TODO: Print program introduction
print("Power and root calculator", end = "\n\n")

# TODO: Collect user information

# TODO: Perform calculations using functions

# TODO: Use suffix to get the proper number suffix: 1st, 2nd...
num_suffix = suffix.determine(user_pow)

# TODO: Print results for both computations using same power
print(f"{user_num} raised to the {user_pow}{num_suffix} power: {raised}")
print(f"{user_num} taken to the {user_pow}{num_suffix} root: {rooted}")
