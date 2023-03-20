import json

def load_file(filename: str = "") -> dict:
    """ Loads a file by name """
    with open(filename) as fh:
        return json.load(fh)

def save_file(filename: str = "", data: dict = {}) -> None:
    """ Saves data to a file by name """
    with open(filename, "w") as fh:
        json.dump(data, filename)

# TODO: Write function to tally votes

# TODO: Write function to cast a vote

# TODO: Write function to conveniently print ballot on demand
    
def main():
    votes = load_file("data/votes.json")
    # TODO: User gets _3_ votes -- that's it!
    print("VOTING FINISHED! FINAL WINNER:", end = "\n\n")
    # TODO: Determine winner

if __name__ == "__main__":
    main()