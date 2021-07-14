from glass_tank import Iguana, Snake, Scorpion, Tarantula, Turtle
from petting_area import Donkey, Dog, Cat, Llama, Goat
import petting_area
from pond import Fish, Duck, Eel, Frog, Beaver
from attractions import SnakePit, PettingZoo, Wetlands

# iggy = Iguana("Iggy", "Green", "Crickets")
# sylvia = Snake("Sylvia", "Python", "Mice")
# tom = Turtle("Tom", "Snapping", "Broccoli")
# sally = Scorpion("Sally", "Emperor", "Lizards")
# terry = Tarantula("Terry", "Mexican Red-Knee", "Grasshoppers")

dan = Donkey("Dan", "Miniature", "Morning", "Hay", 1234)
# doug = Dog("Doug", "Labrador", "Morning", "Kibble")
# cynthia = Cat("Cynthia", "Siamese", "Midday", "Meow Mix")
# larry = Llama("Larry", "Llama", "Evening", "Grass")
# george = Goat("George", "Mountain", "Evening", "Grass")

# fred = Fish("Fred", "Goldfish", "Algae")       
# dorian = Duck("Duck", "Crested", "Bread")
# ed = Eel("Ed", "Giant Moray", "Goldfish")
# frank = Frog("Frank", "Tree frog", "Flies")
# ben = Beaver("Ben", "North American", "Mushrooms")


my_zoo = PettingZoo("devin's zoo", "you pet things")
my_zoo.add_animal(dan)
print(my_zoo.last_animal_added)


