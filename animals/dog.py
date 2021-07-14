from movements.slithering import Slithering
from animals import Animal
from movements import Walking, Swimming

class Dog(Animal, Walking, Swimming):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)  
        Swimming.__init__(self)
        Walking.__init__(self)
        self.shift = shift