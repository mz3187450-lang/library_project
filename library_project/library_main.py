
from library_function import issue_book
from library_function import return_book
from library_function import show_books
from library_function import show_members
from library_function import report
from library_function import add_book
from library_function import register_member
from library_project import Library
lib = Library()
while True:
    print("========== Menu ==========")
    print("1: Add Book")
    print("2: Register Member")
    print("3: issue books")
    print("4: Return books")
    print("5:show all books")
    print("6:show all members")
    print("7:report")
    print("8:exit")
    choice = input("enter number:")
    if choice =="1":
        add_book(lib)
    elif choice =="2":
        register_member(lib)
    elif choice =="3":
        issue_book(lib)
    elif choice =="4":
        return_book(lib)
    elif choice =="5":
        show_books(lib)
    elif choice =="6":
        show_members(lib)
    elif choice =="7":
        report(lib)
    elif choice =="8":
        print("Bye!")
        break
    else:
        print("you enter wrong option")

