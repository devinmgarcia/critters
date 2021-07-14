from datetime import date

class Iguana:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.walking = True
     
class Snake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class Turtle:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.walking = True
      
class Scorpion:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Tarantula:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

iggy = Iguana("Iggy", "Green")
sylvia = Snake("Sylvia", "Python")
tom = Turtle("Tom", "Snapping")
sally = Scorpion("Sally", "Emperor")
terry = Tarantula("Terry", "Mexican Red-Knee")