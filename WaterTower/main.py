# TODO: Import the water tower
# import Pump
from WaterTower import Tower

def main():
    tower = Tower()
    tower.fill()
    print(tower)
    
    while tower.level > 20:
        tower.dispense(volume = 40)
    print(tower)
if __name__ == "__main__":
    main()