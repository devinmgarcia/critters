class Attraction:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f'{self.name} ({len(self)} animals)'

    def __len__(self):
        return len(self.animals)


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

