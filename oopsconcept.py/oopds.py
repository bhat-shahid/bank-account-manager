class Book:
    def __init__(self, title, author, copies):
        self.__title=title
        self.__author=author
        self.__copies=copies
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_copies(self):
        return self.__copies
    def set_title(self,new_title):
        if isinstance(new_title, str) and new_title != "":
            self.__title=new_title
        else:
            print("Invalid Title")
    def set_author(self,new_author):
        if isinstance(new_author, str) and new_author != "":
            self.__author=new_author
        else:
            print("Invalid Author")
    def add_copies(self,number):
        if isinstance(number, int) and number > 0:
            self.__copies+=number
        else:
            print("Invalid Number of Copies")
    def borrow_book(self):
        if self.__copies > 0:
            self.__copies-=1
        else:
            print("No Copies Available")
    def return_book(self):
        self.__copies+=1
book = Book("Python Basics", "John Smith", 3)
print(book.get_copies())
book.borrow_book()
print(book.get_copies())
book.borrow_book()
print(book.get_copies())
book.borrow_book()
print(book.get_copies())
book.borrow_book()
print(book.get_copies())
book.return_book()
print(book.get_copies())
book.set_title("") 
book.add_copies(-5)
book.add_copies(5)
print(book.get_copies())