class Library:

    def __init__(self,list_of_books,library):
        self.l=list_of_books
        self.nameoflib=library
        self.d ={}

    def display_books(self):
        print(f"The books in this library are -->{self.l}")

    def lend_book(self):
        self.book=(input("Which book do you want: "))
        if self.book in self.l:
            self.person_name =input("What is your name")
            self.d[self.book]=self.person_name
            self.l.remove(self.book)
            print(self.d)
        else:
            print(f"Sorry the book is unavailable and the person that holds this book is '{self.d[self.book]}'")

    def add_book(self):
        i=input("Which book do you want to donate: ")
        self.l.append(i)

    def return_book(self):
        x = input("Please enter your book which you want to return: ")
        del self.d[x]
        self.l.append(x)

if __name__=="__main__":
    obname=input("Please enter your object name")
    print("Enter list of books you hold in your library: ")
    booklist=input().split(",")
    libname=input("Please enter your library name:")
    obname=Library(booklist,libname)

    print("Enter 1 for displaying all books of library\n Enter 2 for lending book\n Enter 3 for adding or donating book\n Enter 4 for returning book\n Enter 0 to exit\n ")
    while(True):
        ab=int(input())
        if ab==0:
            break
        elif ab==1:
            obname.display_books()
        elif ab==2:
            obname.lend_book()
        elif ab==3:
            obname.add_book()
        elif ab==4:
            obname.return_book()
        else:
            print("Please check your input")

    print("The books which are lended are -->")
    print(obname.d)
