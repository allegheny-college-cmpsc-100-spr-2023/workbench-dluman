import json
from Pump import Pump

# TODO: Create Tower class
class Tower:

    def __init__(self):
        """ Constructor: basic 'blueprint' """
        # __init__ializing the pump
        self.pump = Pump()
        with open(".tower_fill", "r") as fill_data:
            data = json.load(fill_data)
        self.level = data["level"]
        self.capacity = data["capacity"]
    
    def __str__(self) -> str:
        return f"FILL LEVEL: {self.level}"
    
    def fill(self) -> bool:
        # This uses Pump to get either 20 or 0
        flow = self.pump.use()
        if flow and self.is_not_full():
            self.level += flow
            self.record()
            return True
        return False
        
    def dispense(self, volume: float = 20) -> None:
        self.level -= volume
        self.record()
            
    def record(self) -> None:
        data = {
            "level": self.level,
            "capacity": self.capacity
        }
        with open(".tower_fill", "w") as fill_data:
            # Send the data, then the file
            json.dump(data, fill_data)

    def is_not_full(self) -> bool:
        return self.level < self.capacity
    
    def is_empty(self) -> bool:
        return self.level > 0