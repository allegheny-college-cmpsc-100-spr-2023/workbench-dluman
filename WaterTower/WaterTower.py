import json

# TODO: Create Tower class

    # TODO: Create constructor which:
    #       0. Takes an explicit pump parameter
    #       1. Connects to the pump
    #       2. Loads a file called ".tower_fill"
    #       3. Sets its level and capacity from the file
    
    # TODO: Create a __str__ method to provide the level of
    #       the tower at any given moment using an f-string
    
    # TODO: Write fill method which:
    #       0. Takes no explicit parameters
    #       1. Returns a boolean
    #       2. Ensures there's still tower capacity
    #       3. Uses the pump if possible
    #       4. Adds the flow level to the tower level
    #       5. Records the new level

    # TODO: Write a dispense method which:
    #       0. Takes no explicit parameters
    #       1. Takes a parameter for a given volume
    #       2. Ensures that the tower has that much water
    #       3. Decrements the level by the volume dispensed
    #       4. Records the new level

    # TODO: Write a record method which:
    #       1. Takes no explicit parameters
    #       2. Sets up a data dictionary with level and capacity as keys
    #       3. Writes the new levels to the .tower_fill file

    # TODO: Write a method called "is_full" which:
    #       0. Takes no explicit parameters
    #       1. Returns a boolean, which
    #       1a. Tells us if the level is over capacity

    # TODO: Write a methods called "is_empty" which:
    #       0. Takes no explicit parameters    
    #       1. Returns a boolean, which
    #       1a. Tells us if the level is above 0