class Book:
    def __init__(self, title, author):
        self.title = title                  # Public attribute
        self.author = author                # Public attribute
        self._is_checked_out = False        # Private attribute (single underscore)

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as available (not checked out)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out

    def __str__(self):
        """Readable string representation of a book."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Adds a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """Returns a book by title if it's checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' was not checked out.")

    def list_available_books(self):
        """Prints all books that are currently available."""
        available = [book for book in self._books if book.is_available()]
        for book in available:
            print(book)
