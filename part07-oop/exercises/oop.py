
class Book:
    def __init__(self, title, author, pages):
        self.author = author
        self.title = title
        self.pages = pages

    def summary(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")
    
my_book = Book("War and Peace", "Leo Tolsy", 1225)
print(my_book.title)
print(my_book.author)
print(my_book.pages)