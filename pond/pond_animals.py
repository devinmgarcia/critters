from datetime import date

class Fish:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"
    
    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Duck:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.walking = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
     
class Eel:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.slithering = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
     
class Frog:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
      
class Beaver:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.walking = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
     

fred = Fish("Fred", "Goldfish", "Algae")       
dorian = Duck("Duck", "Crested", "Bread")
ed = Eel("Ed", "Giant Moray", "Goldfish")
frank = Frog("Frank", "Tree frog", "Flies")
ben = Beaver("Ben", "North American", "Mushrooms")

