class Book:
    def __init__(self,title ,author):
        self.title = title
        self.author = author
        self.borrowed_books =[]
    def __eq__(self,other):
        if isinstance(other,str):
            return self.title == other
        if isinstance(other,Book):
            return self.title == other.title
        return False
a = Book("python","al")
print("Python" in ["Python", "Java"])      # string in strings list
print("Python" in [Book("Python", "Eric")]) # string in objects list
