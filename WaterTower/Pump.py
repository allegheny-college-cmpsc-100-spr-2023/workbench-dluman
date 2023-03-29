import json

class Pump:

    def __init__(self):
        """ Constructor """
        self.throughput = 20

    def __str__(self) -> str:
        """ String representation """
        return str(self.throughput)

    def request_capacity(self) -> bool:
        """ Checks if there's enough water in the reservoir """
        with open("/world/reservoir", "r") as fh:
            self.reservoir = json.load(fh)
        return self.reservoir["level"] >= self.throughput

    def update_capacity(self) -> None:
        with open("/world/reservoir", "w") as fh:
            self.reservoir["level"] -= self.throughput
            json.dump(self.reservoir, fh)

    def use(self) -> int:
        if self.request_capacity():
            self.update_capacity()
            return self.throughput
        return 0