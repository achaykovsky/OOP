from Library.Transaction import Transaction


class Borrow(Transaction):
    def __init__(self, book, user, librarian):
        super().__init__(book, user, librarian)

