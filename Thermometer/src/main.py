#!/usr/bin/python

"""
Temperature converstion program used to demonstrate:

* interactive programs
* data types
* basic computation

This program serves as part of the Allegheny College CMPSC 100: Computational
Expression course.
"""

def main():
    
    # TODO: Print program name
    print("Temperature conversion program")
    # TODO: Request user input
    temperature = input("Enter a temperature in F: ")
    # TODO: Perform calculation
    temp_in_f = int(temperature)
    temp_in_c = temp_in_f - 32
    temp_in_c *= 5 / 9
    # TODO: Report result
    final_temp = int(temp_in_c)
    print(f"{final_temp} C")

if __name__ == "__main__":
    main()
