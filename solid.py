from abc import ABC, abstractmethod 


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'
    
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: int):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass

class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str, year: int):
        if any(book.title == title for book in self.books):
            print("A book with this title already exists!")
            return
        
        try:
            year = int(year)
        except ValueError:
            print("Invalid year! Year must be a number!")

        self.books.append(Book(title, author, year))
        print(f'Book "{title}" added successfully!')

    def remove_book(self, title: str):
        initial_count = len(self.books)
        self.books = [book for book in self.books if book.title != title]

        if len(self.books) < initial_count:
            print(f'Book "{title}" removed successfully!')
        else:
            print(f'Book "{title}" not found!')        
    
    def show_books(self):
        if not self.books:
            print("No books in the library!")
            return
        
        for book in self.books:
            print(book)

class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int):
        self.library.add_book(title, author, year)

    def remove_book(self, title: str):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()

def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command: (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter title:").strip()
                author = input("Enter author:").strip()
                year = input("Enter year:").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove:").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()        
            case "exit":
                print("Goodbye!")
                break
            case _:
                print("Invalid command! Please try again.")

if __name__ == "__main__":
    main()

# ("The Catcher in the Rye", "J.D. Salinger", 1951)
# ("To Kill a Mockingbird", "Harper Lee", 1960)
# ("1984", "George Orwell", 1949)
# ("Brave New World", "Aldous Huxley", 1932)
