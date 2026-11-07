class Book:
    def __init__(self,title,author,is_available = True):
        self.title = title
        self.author = author 
        self.is_available = is_available
    def __str__(self):
        return f"title:{self.title} - Author:{self.author} - is_available{self.is_available}"

    def __repr__(self):
        return f"title:'{self.title}' - Author:'{self.author}' - is_available:{self.is_available}"
    def __eq__(self, other):
        if isinstance(other,str):#tell the object which class it to belong and its data type
            return self.title == other
        if isinstance(other,Book):
            return self.title == other.title
        return False

class Member:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.borrowed_books = []
    def __str__(self):
        return f"name:{self.name} - ID:{self.id} - borrowed_books:{self.borrowed_books}"
    def __repr__(self):
        return f"mem_name:{self.name} - mem_ID:{self.id} - book_borrowed:{self.borrowed_books}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_books(self,book):
        self.books.append(book)

    def register_members(self,member):
        self.members.append(member)