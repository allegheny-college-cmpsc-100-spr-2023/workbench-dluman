#!/usr/bin/python

from RegistrationSystem import *

"""
A people registration system to demonstrate:

* lists
* for loop iteration
* while loop iteration
* program design

This program serves as part of the Allegheny College CMPSC 100: Computational
Expression course.

A note about this exercise: assume that ROWS And COLS exist and represent lists
storing the individual column headers and row data
"""

def display_results(rows: list = []) -> None:
    """ Pass filtered results to table display """
    if not rows:
        rows = ROWS
    for idx in range(len(ROWS)):
        ROWS[idx] = [str(elem) for elem in ROWS[idx]]
    display_table(rows = rows)

def gets_shirt(registrant: list = []) -> bool:
    # TODO: Filter list for folks buying shirts
    return False

def set_limit(number: str = "") -> int:
    """ Set a numerical age limit """
    # TODO: Return an int if a number provided
    return number

def average(column: str = "") -> int:
    """ Computes the average of a column """
    total = 0
    # TODO: Compute the average of a column
    return total / len(ROWS)

def create_row() -> list:
    """ Create a list-as-row """
    fname = input("First name: ")
    lname = input("Last name: ")
    age = input("Age: ")
    shirts = input("How many shirts: ")
    # Return the correct information as a separate list
    return [

    ]

def main():
    # Menu
    print("REGISTRATION STATION", end = "\n\n")
    print("Choose from the following options:", end = "\n")
    print("1. T-Shirt orders")
    print("2. All participants above given age")
    print("3. Statistics view")
    print("4. Add a participant")
    print("5. Display all registrants")
    print("0. Exit")

    # Loop through
    while True:
        # Resolve menu
        choice = int(input("Choose an option by number: "))
        # If exit, well, exit
        if choice == 0:
            break
        # Create list to store the results of filterings
        # TODO: Complete the functionality
        if choice == 5:
            display_results()

if __name__ == "__main__":
    main()