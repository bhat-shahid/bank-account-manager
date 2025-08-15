class LibraryBook:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author=author
        self.is_borrowed = is_borrowed
    def barrow_book(self):
        if self.is_borrowed==False:
            self.is_borrowed=True
            print("You have borrowed the book.")
        else:
            print("The book is already borrowed.")
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            print("Book returned successfully.")
        else:
            print("This book wasn't borrowed.")
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: Avalible")
book1 = LibraryBook("Atomic Habits", "James Clear")
book1.display_info()
book1.barrow_book()
book1.barrow_book()
book1.return_book()
book1.return_book()
book1.display_info()