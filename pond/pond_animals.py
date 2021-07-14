from datetime import date

class Fish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        

class Duck:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.walking = True
     
class Eel:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.slithering = True
     
class Frog:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
      
class Beaver:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.walking = True
     

fred = Fish("Fred", "Goldfish")       
dorian = Duck("Duck", "Crested")
ed = Eel("Ed", "Giant Moray")
frank = Frog("Frank", "Tree frog")
ben = Beaver("Ben", "North American")