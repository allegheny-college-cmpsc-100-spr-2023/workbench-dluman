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
"""

def display_results(rows: list = []) -> None:
    """ Pass filtered results to table display """
    if not rows:
        rows = ROWS
    for idx in range(len(ROWS)):
        ROWS[idx] = [str(elem) for elem in ROWS[idx]]
    display_table(rows = rows)

def gets_shirt(registrant: list = []) -> bool:
    """ Assess if a partcipant ordered a shirt """
    ordered_shirt = int(registrant[4])
    if ordered_shirt > 0:
        return True
    return False

def set_limit(number: str = "") -> int:
    """ Set a numerical age limit """
    if number:
        return int(number)
    return number

def average(column: str = "") -> int:
    """ Computes the average of a column """
    total = 0
    idx = COLS.index(column)
    for row in ROWS:
        total += int(row[idx])
    return total / len(ROWS)

def create_row() -> list:
    """ Create a list-as-row """
    fname = input("First name: ")
    lname = input("Last name: ")
    age = input("Age: ")
    shirts = input("How many shirts: ")
    return [
        len(ROWS) + 1,
        fname,
        lname,
        age,
        shirts
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
        people = []  
        if choice == 1:
            for person in ROWS:
                if gets_shirt(person):
                    people.append(person)
            display_results(people)
        if choice == 2:
            limit = set_limit(input("Minimum age: "))
            for person in ROWS:
                if int(person[3]) >= limit:
                    people.append(person)
            display_results(people)
        if choice == 3:
            avg_age = average("age")
            avg_shirts = average("shirt")
            data = [['','','',avg_age,avg_shirts]]
            display_results(data)
        if choice == 4:
            print("Let's gather some data:", end = "\n\n")
            row = create_row()
            ROWS.append(row)
            save_file()
        if choice == 5:
            display_results()

if __name__ == "__main__":
    main()