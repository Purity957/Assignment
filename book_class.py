class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def book_info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

    def read(self):
        return f"You are now reading '{self.title}'."

# Creating objects
book1 = Book("Things Fall Apart", "Chinua Achebe", 209)
book2 = Book("Harry Potter", "J.K. Rowling", 350)

# Using methods
print(book1.book_info())
print(book1.read())

print(book2.book_info())
print(book2.read())
