class Books:
    def __init__(self, author_name:str, title:str, book_id:int):
        self.author_name = author_name
        self.title = title
        self.book_id = book_id

    def __str__(self):
        return f"ID: {self.book_id}, Author: {self.author_name}, Title: {self.title}"


class Library:
    def __init__(self, name:str):
        self.name = name
        self.books = []

    def add_book(self, book:Books):
        self.books.append(book)

    def remove_book(self, book_id:int):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return True
        return False

    def list_books(self):
        return [str(book) for book in self.books]



library = Library("Vienna Library")

book1 = Books(author_name="Rebecca Yarros", title="Fourth Wing", book_id=1)
book2 = Books(author_name="Marc-Uwe Kling", title="Känguru-Chroniken", book_id=2)

library.add_book(book1)
library.add_book(book2)
print(library.list_books())

library.remove_book(1)
print(library.list_books())

library.add_book(book1)
library.remove_book(2)
print(library.list_books())

library.remove_book(1)
print(library.list_books())