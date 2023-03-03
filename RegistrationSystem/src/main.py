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
    # If no parameter exists, default to the global
    if not rows:
        rows = ROWS
    # For each index, convert it to a string for rich
    for idx in range(len(ROWS)):
        ROWS[idx] = [str(elem) for elem in ROWS[idx]]
    # Display the table pretty print style
    display_table(rows = rows)

def gets_shirt(registrant: list = []) -> bool:
    """ Assess if a partcipant ordered a shirt """
    # Get the list address for item number 5 (index 4)
    ordered_shirt = int(registrant[4])
    # If the quantity of shirts is greater than 0, return True
    # for a person
    if ordered_shirt > 0:
        return True
    # In every other case return False for a person
    return False

def set_limit(number: str = "") -> int:
    """ Set a numerical age limit """
    # If a number exists at all, convert to integer version
    if number:
        return int(number)
    # Return the data in whatever version is appropriate
    return number

def average(column: str = "") -> int:
    """ Computes the average of a column """
    # Set a catch-all variable to 0 to count number of items
    total = 0
    # Get the index of a given column by name to find the
    # corresponding position in the list
    idx = COLS.index(column)
    # For each row in the larger data set
    for row in ROWS:
        # Add the integer representation of the file to the
        # running total
        total += int(row[idx])
    # Return the running total divided by the number of items,
    # which is the textbook definition of an average
    return total / len(ROWS)

def create_row() -> list:
    """ Create a list-as-row """
    # Take inputs for each necessary item of data
    fname = input("First name: ")
    lname = input("Last name: ")
    age = input("Age: ")
    shirts = input("How many shirts: ")
    # Return data in list form
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
            # Get average of age column
            avg_age = average("age")
            # Get average of shirts column
            avg_shirts = average("shirt")
            # Reset the dataset to a new one-row set
            people.append(['','','',avg_age,avg_shirts])
            display_results(people)
        if choice == 4:
            print("Let's gather some data:", end = "\n\n")
            row = create_row()
            ROWS.append(row)
            save_file()
        if choice == 5:
            display_results()

if __name__ == "__main__":
    main()