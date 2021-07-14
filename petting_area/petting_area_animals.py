from datetime import date

class Donkey:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

class Dog:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.walking = True
        self.shift = shift

class Cat:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

class Llama:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

class Goat:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift


dan = Donkey("Dan", "Miniature", "Morning")
doug = Dog("Doug", "Labrador", "Morning")
cynthia = Cat("Cynthia", "Siamese", "Midday")
larry = Llama("Larry", "Llama", "Evening")
george = Goat("George", "Mountain", "Evening")
