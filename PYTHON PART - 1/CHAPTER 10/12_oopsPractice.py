class Programmer :
    company = "Microsoft"
    empId = None
    salary = None
    name = None
    points = None

    def __init__(self,x) :
        self.empId = x
        print("Constructor Invoked")

    def setData(self,y,z,k) :
        self.salary = y
        self.name = z
        self.setData2(k)#syntax


    def setData2(self,k) :
        self.points = k

    def printData(self) :
        print(self.company)
        print(self.empId)
        print(self.salary)
        print(self.name)
        print(self.points)

    @staticmethod 
    def greet() :
        print("End of the printData")


emp1 = Programmer(101)
emp2 = Programmer(102)

emp1.setData(100000,"harry",100)
emp2.setData(200000,"harish",200)

emp1.printData()
Programmer.greet()
emp2.printData()
Programmer.greet()

