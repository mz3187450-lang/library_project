from library_project import Book
from library_project import Member
def add_book(lib):
    while True:
        title = input("enter the book title:")
        checker = True
        for book in lib.books:
            if book.title.lower() == title.lower():
                print("same book cannot be add twice")
                checker = False
        if checker == False:
            continue
        author = input("enter name of book author:")
        break
    book1 = Book(title,author)
    lib.add_books(book1)

def register_member(lib):
    name = input("enter your name:")
    while True:
        member_id = input("enter your id:")
        checker = True
        for member in lib.members:
            if member.id.lower() == member_id.lower():
                print("the current id is taken by someone")
                checker = False
        if checker == False:
            continue
        break
    member1 = Member(name,member_id)
    lib.register_members(member1)

    
def issue_book(lib):
    id = input("enter your id:")
    checker = True
    for  mem_id in lib.members:
        if id.lower() == mem_id.id.lower():
            if len(mem_id.borrowed_books) < 3:
                ask_book = input("enter book name you want :")
                checker2 = True
                for book in lib.books:
                    if ask_book.lower() == book.title.lower():
                        if book.is_available == True:
                            mem_id.borrowed_books.append(book)
                            print("the book is issued")
                            book.is_available = False
                            checker = False
                            checker2 = False
                        else:
                            print("the book is not available")
                            checker = False
                            checker2 = False
                if checker2 == True:
                    print("we have not that book")
                    checker = False
            
            else:
                print("the user already take 3 books")
                checker = False
    if checker == True:
        print("you enter wrong id")


def return_book(lib):
    id = input("enter your id:")
    checker = True
    checker2 = True
    for  mem_id in lib.members:
        if id == mem_id.id:
           checker2 = False
           ask_book =input("enter book name you issued:")
           for book in lib.books:
               if ask_book.lower() ==book.title.lower():
                    if ask_book in mem_id.borrowed_books:#here we use __eq__ in book class to compate str and book object
                        book.is_available = True
                        mem_id.borrowed_books.remove(book)
                        print("the book is returned")
                        checker = False
                    else:
                        print("this book is not issued to you")
                        checker = False
           if checker == True:
               print("this book not belongs to library")
    if checker2 == True:
        print("the id is not registered")
def show_books(lib):
    for book in lib.books:
        print(f"title:{book.title} - author:{book.author} - is_available:{book.is_available}")
def show_members(lib):
    for member in lib.members:
        print(f"name:{member.name} - ID:{member.id} - borrowed_books:{member.borrowed_books}")
def report(lib):
    for member in lib.members:
        print(f"{member.name} {(member.id)}")
        if not member.borrowed_books:
            print("  - NO Books")
        else:
            for book in member.borrowed_books:
                print(f"  -{book.title}")   
           


    
   
