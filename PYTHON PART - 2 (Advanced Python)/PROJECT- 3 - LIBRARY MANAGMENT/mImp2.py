class Library :
    bookList = []

    def __init__(self,listOfBooks) :
        self.bookList = listOfBooks

    def printBookList (self) :

        for index,item in enumerate(self.bookList) :
            print((index+1),end=")")
            print("",item)

    def requestBook (self,reqList) :
        for i in range (len(reqList)) :
            if(reqList[i] in self.bookList) :
                print(f"*************The book {reqList[i]} is issued*************************")
                self.bookList.remove(reqList[i])

            else :
                print(f"*************Sorry The book {reqList[i]} is not available*************")

    
    def returnBook (self,retList) :
        for item in retList :
            self.bookList.append(item)
            print(f"******************The book {item} is submitted.Thank You******************")


studentList = []

class Student :

    reqList = []
    retList = []
    name = None
    serialNo = None
    index = 1

    def __init__(self,num) :

        self.serialNo = num
        self.name = input(f"Enter name {self.index} Please: \n")


    def requestBook (self) :
        num = input("Enter the number of books :\n")
        num = int(num)
        self.reqList = []

        for i in range(num) :
            book = input(f"Enter the book {i+1} :\n")
            self.reqList.append(book)

        return self.reqList

    def returnBook (self) :
        num = input("Enter the number of books :\n")
        num = int(num)
        self.retList = []


        for i in range(num) :
            book = input(f"Enter the book {i+1} :\n")
            self.retList.append(book)

        return self.retList
