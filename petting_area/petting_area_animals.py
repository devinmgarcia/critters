from datetime import date

class Donkey:
    def __init__(self, name, species, shift, food, chip_number):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
        self.__chip_number = chip_number

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, number):
        pass

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Dog:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.walking = True
        self.shift = shift
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Cat:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Llama:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Goat:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')



