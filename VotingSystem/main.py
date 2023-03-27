import json

def load_file(filename: str = "") -> dict:
    """ Loads a file by name """
    with open(filename) as fh:
        return json.load(fh)

def save_file(filename: str = "", data: dict = {}) -> None:
    """ Saves data to a file by name """
    with open(filename, "w") as fh:
        json.dump(data, filename)

def tally_votes(votes_cast: list = [], candidates: dict = {}) -> dict:
    # Go vote by vote and organize it
    for ballot in votes_cast:
        #print(ballot)
        if ballot in candidates:
            candidates[ballot] += 1
        else:
            candidates[ballot] = 1
    return candidates

# TODO: Write function to conveniently print ballot on demand
    
def main():
    votes = load_file("data/votes.json")
    # Define empty dictionary
    candidates = tally_votes(votes_cast = votes)
    # Establish a blank list to "store" votes
    votes_to_cast = []
    # Allow user to vote until list has 3 items
    while len(votes_to_cast) < 3:
        # Take in user vote
        vote = input("ENTER NAME TO VOTE FOR: ")
        # Add to vote list
        votes_to_cast.append(vote)
    # Send _ONCE_ as completed list of 3 items
    candidates = tally_votes(votes_cast = votes_to_cast)
    print("VOTING FINISHED! FINAL WINNER:", end = "\n\n")
    max_votes = 0
    for electee in candidates:
        votes_for = candidates[electee] # <--- looking for name key of candidates
        if votes_for > max_votes:
            max_votes = votes_for
            winner = e0lectee
    print(candidates)
    print(f"WINNER: {winner}, VOTES: {max_votes}!")

if __name__ == "__main__":
    main()