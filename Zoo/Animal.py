import uuid


class Animal:
    def __init__(self, name: str):
        self.name = name
        self.id = uuid.uuid4()
        self.type = self.__class__.__name__

    def make_sound(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def __str__(self):
        return f"{self.name} (ID: {self.id}) the {self.type}"
