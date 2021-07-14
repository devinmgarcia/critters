from animals import Animal
from movements import Swimming, Slithering

class Eel(Animal, Swimming, Slithering):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)  
        Swimming.__init__(self)
        Slithering.__init__(self)