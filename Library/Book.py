class Book:
    def __init__(self, book_id, title, authors, amount):
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.amount = amount

    def get_book(self, book_id):
        return self

    def get_amount(self):
        return self.amount

    def borrow_book(self):
        if self.amount > 0:
            self.amount -= 1
            return 1
        else:
            print(f"The book {self.title} out of stock")
            return -1

    def return_book(self):
        self.amount += 1
        print(f"The book {self.book_id} was returned")