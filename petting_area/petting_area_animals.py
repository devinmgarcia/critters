from datetime import date
from animals import Animal

class Donkey(Animal):
     def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)      
        self.walking = True
        self.shift = shift

class Dog(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)  
        self.swimming = True
        self.walking = True
        self.shift = shift

class Cat(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)  
        self.walking = True
        self.shift = shift

class Llama(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)  
        self.walking = True
        self.shift = shift
    def feed(self):
        print(f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')

class Goat(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)  
        self.walking = True
        self.shift = shift
   



