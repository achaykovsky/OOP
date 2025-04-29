from Animal import Animal
from Cell import Cell


class Zoo:
    def __init__(self):
        self.cells = {}

    def add_cell(self, species: str):
        if species not in self.cells:
            self.cells[species] = Cell(species)
        else:
            raise ValueError("Cell for this species already exists")

    def add_animal_to_cell(self, animal: Animal):
        species = animal.type
        if species in self.cells:
            self.cells[species].add_animal(animal)
        else:
            raise ValueError("Cell for this species does not exist")

    def get_cells(self):
        return self.cells

    def __str__(self):
        return '\n'.join(str(cell) for cell in self.cells.values())
