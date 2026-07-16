# creating class
class Book:
    def __init__(self, title, author, pages):
        self.author = author
        self.title = title
        self.pages = pages

    def summary(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"
    
# putting values 
my_book = Book("War and Peace", "Leo Tolsy", 1225)
print(my_book.title)
print(my_book.author)
print(my_book.pages)
my_book.summary()
print(my_book)


second_book = Book("1984", "George Orwell", 328)
second_book.summary()

class Ebook(Book):
    def __init__(self, title, author, pages, file_size_mb):
        super(). __init__(title, author, pages)
        self.file_size_mb = file_size_mb
    
    def summary(self):
        print(f"{self.title} by {self.author}, {self.pages} pages, {self.file_size_mb}MB")

my_ebook = Ebook("Dune", "Frank Herbert", 412, 3.5)
my_ebook.summary()