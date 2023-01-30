#!/usr/bin/python

"""
A program to determine what grammatical suffix follows a given number
"""

def determine(number: int = 0) -> str:
    digits = str(number)
    suffixes = {
        "1": "st",
        "2": "nd",
        "3": "rd"
    }
    try:
        return suffixes[digits[-1]]
    except KeyError:
        return "th"
