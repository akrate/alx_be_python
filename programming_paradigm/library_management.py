class Book:
    def __init__(self,title: str,author: str):
        self.title = title
        self.author = author
        self._is_checked_out = false
    def check_out(self):
        self._is_checked_out = true
    def return_book(self):
        self._is_checked_out = false
    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self,book):
        self.books.append(book)

    def check_out_book(self, title):
         for book in self._books:
         if book.title == title and book.is_available():
             book.check_out()
             print(f"Checked out: {title}")
             return print(f"Book '{title}' is not available to check out.")
            
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {title}")
                return
        print(f"Book '{title}' was not checked out.")

    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No available books.")
            return
        for book in available:
            print(f"{book.title} by {book.author}")