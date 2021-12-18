class Employee :
    company = "Microsoft"
    num = 100
    test = None

    def setTest(self,int) :
        self.test = int

    def getDetails (self) :
        print("The name of the company is :",self.company)


class Programmer(Employee) :
    language = "Python"
    #company = "YouTube"#overwrites

    def getLanguage(self) :
        print(f"The language is {self.language}")

    def getDetails (self) :#overwriting
        print("The name of language is :",self.language)

pgm = Programmer()
pgm.setTest(4)
emp = Employee()
emp.setTest(5)
emp.getDetails()
pgm.getDetails()
print(emp.num)
print(emp.test)# we can access even the class attributes like
#this
print(pgm.num)
print(pgm.test) 


