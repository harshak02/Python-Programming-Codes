class Employee :
    company = "Google"
    salary = None

    def printData(self) :
        print(f"The company is {self.company} and salary is {self.salary}")


emp1 = Employee()
emp2 = Employee()

emp1.salary = 100000
Employee.company = "Youtube"#changing (class attribute)
emp2.salary = 500000

emp1.printData()#Employee.printData(emp1)->alternative
emp2.printData()

