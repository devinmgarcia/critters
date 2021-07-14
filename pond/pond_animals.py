from datetime import date
from animals import Animal

class Fish(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)  
        self.swimming = True

class Duck(Animal):
   def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)  
        self.swimming = True
        self.walking = True
     
class Eel(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)  
        self.swimming = True
        self.slithering = True
     
class Frog(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)  
        self.swimming = True
      
class Beaver(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)  
        self.swimming = True
        self.walking = True
    
     



