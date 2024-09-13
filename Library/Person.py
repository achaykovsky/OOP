from abc import ABC


class Person(ABC):
    def __init__(self, id, name, last_name):
        self.id = id
        self.name = name
        self.last_name = last_name