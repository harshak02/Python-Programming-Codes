class Employee : 
    salary = None
    increment = None
    # salaryAfterIncrement = None

    def __init__(self,num1,num2) :
        self.salary = num1
        self.increment = num2

    @property # also called getter
    def salaryAfterIncrement (self) :
        result = self.salary + self.increment
        return result

    @salaryAfterIncrement.setter
    def salaryAfterIncrement (self,num) :
        self.salary = num - self.increment

    def printData (self) :
        print("The value of salary is s :",self.salary)
        print("The value of increment is s :",self.increment)
        print("The value of total is s :",self.salaryAfterIncrement)


emp = Employee(1000,2000)
print(emp.salaryAfterIncrement)# gives garbage value
print("******")
emp.salaryAfterIncrement = 4000
emp.printData()




