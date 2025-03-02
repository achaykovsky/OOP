from abc import ABC

from Library.Borrow import Borrow


class Library:
    def __init__(self, books, users, libarians):
        self.books = books
        self.users = users
        self.librarians = libarians
        self.borrows = []

    def borrow_book(self, book_id, user_id, librarian_id):
        book = self.books.get(book_id, -1)
        if book < 0:
            print("Book wasn't found")
        user = self.users.get(user_id, -1)
        librarian = self.libarians.get(librarian_id, -1)
        book.borrow_book()
        borrow = Borrow(book, user, librarian)
        self.borrows.append(borrow)
