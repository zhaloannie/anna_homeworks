import pytest
from classes import Books, Library

class TestLibrary:

    @pytest.fixture
    def library(self):
        return Library("Test Library")

    @pytest.fixture
    def book1(self):
        return Books("Rebecca Yarros", "Fourth Wing", 1)

    @pytest.fixture
    def book2(self):
        return Books("Marc-Uwe Kling", "Känguru-Chroniken", 2)

    def test_add_book(self, library, book1):
        library.add_book(book1)
        assert len(library.books) == 1
        assert library.books[0].book_id == 1

    def test_remove_book(self, library, book1):
        library.add_book(book1)
        result = library.remove_book(1)
        assert result is True
        assert len(library.books) == 0

    def test_remove_non_existing_book(self, library):
        result = library.remove_book(0)
        assert result is False

    def test_list_books(self, library, book1, book2):
        library.add_book(book1)
        library.add_book(book2)
        books_list = library.list_books()
        assert len(books_list) == 2
        assert "Fourth Wing" in books_list[0]
        assert "Känguru-Chroniken" in books_list[1]