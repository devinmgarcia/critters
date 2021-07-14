from animals import Animal
from movements import Walking

class Scorpion(Animal, Walking):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)