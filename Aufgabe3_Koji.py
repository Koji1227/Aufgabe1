# Programmieren vertieft
# Aufgabe 3; 09.05.2024
# Name: Koji Okumura

class Author:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
    
    def __repr__(self):
        return f"{self.last_name}, {self.first_name}"

class Publisher:
    def __init__(self, publisher, place = None):
        self.publisher = publisher
        self.place = place
    
    def __repr__(self):
        return f"{self.place}: {self.publisher}"

class Book:
    def __init__(self, title, year, author, publisher):
        self.title = title
        self.year = year
        self.author = author
        self.publisher = publisher
    
    def __repr__(self):
        return f"Title: {self.title}; Year: {self.year}; Author: {self.author}; Publisher: {self.publisher}"
    
    def get_citation(self):
        return f"{self.author} ({self.year}). {self.title}. {self.publisher}."

if __name__ == "__main__":
    author1 = Author("Hammond", "Michael")
    publisher1 = Publisher("Cambridge University Press", "Cambridge")
    book1 = Book("Python for Linguists", 2018, author1, publisher1)

    print(author1)
    print(publisher1)
    print(book1)
    print(book1.get_citation())

# Feedback: Good solution, prints the single objects and a citation of the book.