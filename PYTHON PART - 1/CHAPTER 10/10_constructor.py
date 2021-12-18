class Employee :
    company = "YouTube"
    salary = None

    def __init__(self):
        print("The employee class created")

    def getData(self,signature) :
        print(f"The company is {self.company} and salary is {self.salary}\n",signature)


    @staticmethod
    def greet() :# dont take the self here
        print("Good! Morning...")


    @staticmethod
    def time() :
        print("The time is 9 a.m")


emp1 = Employee()
emp2 = Employee()

emp1.salary = 1000
emp2.salary = 2000

emp1.getData("Thank you!")
Employee.greet()
Employee.time()#use for static functions
emp2.getData("Thank you!")# Employee.getData(emp2,"Thank You!")
Employee.greet()
Employee.time()
