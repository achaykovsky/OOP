from Elephant import Elephant
from Zoo import Zoo
from Lion import Lion

if __name__ == "__main__":
    zoo = Zoo()
    zoo.add_cell("Dog")
    zoo.add_cell("Elephant")

    simba = Lion(name="Simba")
    dumbo = Elephant(name="Dumbo")

    zoo.add_animal_to_cell(simba)
    zoo.add_animal_to_cell(dumbo)
