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
# Function signature
def raise_to_power(number: float = 0.0, power: float = 1) -> float:
    """ Raises a number to an arbitrary power """
    raised_num = number ** power
    # Sends the number back to the place we left off
    return raised_num

# TODO: Write function to calculates nth root of a number 
#       by raising to fractional power
#   name      parameters-------------------------      return type
def calc_root(number: float = 0.0, root: float = 1) -> float:
    """ Take the nth root of an arbitrary number """
    # 1/power -> root
    nth_root = raise_to_power(number = number, power = 1/root)
    return nth_root

# Print program introduction
print("Power and root calculator", end = "\n\n")

# TODO: Collect user information
user_num = int(input("Enter a base: "))
user_pow = int(input("Enter an exponent: "))

# TODO: Perform calculations using functions
# Function call
raised = raise_to_power(number = user_num, power = user_pow)
rooted = calc_root(number = user_num, root = user_pow)

# TODO: Use suffix to get the proper number suffix: 1st, 2nd...
num_suffix = suffix.determine(user_pow)

# TODO: Print results for both computations using same power
print(f"{user_num} raised to the {user_pow}{num_suffix} power: {raised}")
print(f"{user_num} taken to the {user_pow}{num_suffix} root: {rooted}")
