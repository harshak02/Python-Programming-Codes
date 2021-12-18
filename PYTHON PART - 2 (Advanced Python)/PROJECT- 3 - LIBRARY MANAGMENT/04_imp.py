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


print("=====Welcome=====")
print("")

listOfBooks = ["Telugu","Hindi","English","Maths","Science","Social"]

lib = Library(listOfBooks)

number = input("Enter the number of students :\n")
number = int(number)
print("\nProcessing...\n")

for i in range(number) :
    studentList.append(Student(i+1))
    Student.index +=1


welcomeMsg1 ='''
<----==========Welcome To Central Library==========---->

->powered by VS code (64 bit) and Python 3.9.6(updated)
->desinged by Harsha
'''

welcomeMsg2 ='''
Please Enter the choice from below :-

Enter "1" for : Displaying The Booklist of Library
Enter "2" for : Requesting books from Library
Enter "3" for : Returning books to Library
Enter "4" for : Exiting the Library portal
'''


for i in range(number) :
    print("\nProcessing")
    print(welcomeMsg1)
    print(f"Hello..! Welcome ***{studentList[i].name}***,with Warm regards! ")

    while(True) :

        choice = input(f"{welcomeMsg2} \n")#only one arg must be
        choice = int(choice)
        

        if (choice == 1) :

            print("\nProcessing...\n")
            lib.printBookList()

        elif (choice == 2) :
            
            print("\nProcessing...\n")
            tempList = studentList[i].requestBook()
            lib.requestBook(tempList)

        elif (choice == 3) :
            
            print("\nProcessing...\n")
            tempList = studentList[i].returnBook()
            lib.returnBook(tempList)

        elif (choice == 4) :
            
            print("\nProcessing...\n")
            print(f"Thank You ***{studentList[i].name}*** for using Library Portal...Have a nice day!!")
            break#for single user use exit()

        else :

            print("\nProcessing...\n")
            print("Please enter a valid choice!!")



print("\n*****************Rating time*********************\n")

rate = input("Please applaud my portal by giving rating out of 5 :-) :\n")
rate = int(rate)

if ((rate>=1) and (rate<=3)) :
    print("Thanks for giving rating below 3 we will sort our negatives")

elif (rate==4) :
    print("Thanks for giving 4 star rating you support is our motivation")

else :
    print("Thanks for giving 5 star rating :-)")

