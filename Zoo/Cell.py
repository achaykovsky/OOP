from Animal import Animal


class Cell:
    def __init__(self, species: str):
        self.species = species
        self.animals = []

    def add_animal(self, animal: Animal):
        if animal.type == self.species:
            self.animals.append(animal)
        else:
            raise ValueError("Animal species does not match the cell species")

    def get_num_of_animals_in_cell(self):
        return len(self.animals)

    def __str__(self):
        animal_info = ', '.join(str(animal) for animal in self.animals)
        return f"Cell for {self.species}: {animal_info if animal_info else 'Empty'}"
