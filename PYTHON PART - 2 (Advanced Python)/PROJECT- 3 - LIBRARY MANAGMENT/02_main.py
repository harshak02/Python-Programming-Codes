class Library :
    books = []

    def __init__(self,listOfBooks) :
        self.books = listOfBooks

    def displayAvilableBooks (self) :
        print("The available books in the library are :")
        
        for item in self.books :
            print("  *",end="")
            print(item)#we can use enumerate to index

    def borrowBook (self,bookName) :
        if (bookName in self.books) :
            self.books.remove(bookName)
            print(f"The book - '{bookName}' is issued keep it safe")
            

        else :
            print(f"Sorry the Book - '{bookName}' is not avialable")
            exit()

    
    def returnBook (self,bookName) :
        self.books.append(bookName)
        print(f"The book - {bookName} is submitted back")


class Student :
    bookreq = None
    bookret = None 

    def requestBook (self) :
        self.bookreq = input("Which book do you need from library? \n")
        return self.bookreq

    def returnBook (self) :
        self.bookret = input("Which book will you return to library? \n")
        return self.bookret


if __name__ == "__main__" :

    list1 = ["django","python","webdev","clrs"]

    centralLibrary = Library(list1) 
    harry = Student()

    centralLibrary.displayAvilableBooks()

    book1 = harry.requestBook()
    centralLibrary.borrowBook(book1)
    centralLibrary.displayAvilableBooks()

    book2 = harry.returnBook()
    centralLibrary.returnBook(book2)
    centralLibrary.displayAvilableBooks()


            
