from Library.Person import Person


class User(Person):
    def __init__(self, id, name, last_name):
        super().__init__(id, name, last_name)
