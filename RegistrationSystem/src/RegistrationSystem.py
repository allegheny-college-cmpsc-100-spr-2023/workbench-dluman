import csv

from rich.table import Table
from rich.console import Console

def load_file(filename: str = "") -> list:
    """ Opens a CSV file """
    data = []
    with open(filename, "r") as fh:
        reader = csv.reader(fh)
        for row in reader:
            data.append(row)
    return data

def save_file(filename: str = "data/registrants.csv") -> None:
    """ Saves a CSV file """
    data = [COLS] + ROWS
    with open(filename, "w") as fh:
        writer = csv.writer(fh, delimiter = ",")
        for row in data:
            writer.writerow(row)

def display_table(rows: list = []) -> None:
    """ Display table using rich library """
    table = Table(title="REGISTRATIONS")
    if not rows:
        rows = ROWS
    for col in COLS:
        table.add_column(col)
    for row in rows:
        row = [str(elem) for elem in row]
        table.add_row(*row)
    console = Console()
    console.print(table)

data = load_file("data/registrants.csv")
global COLS
global ROWS
COLS = data[0]
ROWS = data[1:]