students = []

class Simple :

    name = None
    rollno = None 
    marks = None
    index = 1
    index2 = 1

    def __init__(self,rollno) :
        self.rollno = rollno

    def getData(self) :
        self.name = input(f"Name of {self.index} Please :\n")
        self.marks = input(f"Marks of {self.index} Please :\n")
    
    def printData(self) :
        print(f"The name of student {self.index2} is : {self.name}")
        print(f"The rollno of student {self.index2} is : {self.rollno}")
        print(f"The marks of student {self.index2} is : {self.marks}")

num = input("Enter the no. of students :\n")
num = int(num)

for i in range (num) :
    students.append(Simple(i+1))
    students[i].getData()
    Simple.index +=1
    print("")

print("")

for i in range (num) :
    students[i].printData()
    print("")
    Simple.index2 +=1



print("Done!!")

