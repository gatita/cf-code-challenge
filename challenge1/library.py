class Library(object):
    def __init__(self):
        self.shelves = []
    
    def add_shelf(self, shelf):
        self.shelves.append(shelf)
        
    def number_of_shelves(self):
        return len(self.shelves)
           
        
class Shelf(object):
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        if not(book in self.books):
            raise ValueError('Book is not on shelf.')
        self.books.remove(book)
        
    def show_books(self):
        if len(self.books) == 0:
            print 'This shelf contains 0 books.'
        for book in self.books:
            print book.title + ' by ' + book.author

class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def enshelf(self, shelf):
        shelf.add_book(self)
        
    def unshelf(self, shelf):
        shelf.remove_book(self)
        
library = Library()
nonfiction = Shelf()
book1 = Book('Ideas and Opinions', 'Albert Einstein')
book2 = Book('Speak, Memory', 'Vladimir Nabokov')
book3 = Book('The Elements of Style', 'William Strunk and E.B. White')


    

        