class SnakePit:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_animal_added(self):
        return self.animals[-1]

class PettingZoo:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_animal_added(self):
        return self.animals[-1]

class Wetlands:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_animal_added(self):
        return self.animals[-1]

