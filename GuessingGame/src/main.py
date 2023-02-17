#!/usr/bin/python

"""
A number guessing game intended demonstrate:

* booleans
* conditional statements
* conditional logic
* "iteration" -- specifically while loops

This program serves as part of the Allegheny College CMPSC 100: Computational
Expression course.
"""

# Necessary imports
import random

def above_the_number(guess: int = 0, the_number: int = 0) -> bool:
    """ Compares guess to number to check if higher than number """
    return guess > the_number
    
def below_the_number(guess: int = 0, the_number: int = 0) -> bool:
    """ Compares guess to number to check if lower than number """
    return guess < the_number

def outside_the_range(guess: int = 0, low: int = 0, high: int = 1) -> bool:
    return guess > high or guess < low

def main():
    lower_limit = 1
    upper_limit = 2000
    number_to_guess = random.randint(lower_limit, upper_limit)
    game_choice = input(f"I'm thinking of a number between {lower_limit} and {upper_limit}. Guess? ")
    while int(game_choice) != number_to_guess:
        game_choice = input("Wrong guess. Guess again? ")
        if not game_choice:
            game_choice = 0
        game_choice = int(game_choice)
        if game_choice == 0:
            print("Did you enter a number?")
        elif above_the_number(game_choice, number_to_guess):
            print("Looks like you're a little higher than the number.")
        elif below_the_number(game_choice, number_to_guess):
            print("Looks like you're a little lower than the number.")
        elif outside_the_range(guess = game_choice, high = upper_limit, low = lower_limit):
            print("Your guess is outside the range!")
    print("You won!")
    # TODO: While the number guessed doesn't fit the requested criteria,
    #       keep generating

    # TODO: While the user's guess doesn't match the number, keep the
    #       user guessing

    # TODO: If the user gets to this point, they win! Tell 'em

if __name__ == "__main__":
    main()
