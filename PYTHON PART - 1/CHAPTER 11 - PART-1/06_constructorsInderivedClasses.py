class Person :
    country = "India"

    def __init__(self) :
        print("This is the Person Constructor")

    def takeBreathe(self) :
        print("Im breathing")


class Employee(Person) :
    company = "Honda"
    salary = 1000

    def __init__(self) :
        super().__init__()#shall be used for better code
        print("This is the Employee Constructor")

    def getSalary(self) :
        print(f"The salary is {self.salary}")

    def takeBreathe(self):
        super().takeBreathe()
        print("This is updated Im breathing..")


class Programmer(Employee) :
    company = "Fiverr"

    def __init__(self) :
        super().__init__()
        print("This is the Programmer Constructor")

    def getSalary(self):
        print("No salary to rogrammer")


    def takeBreathe(self):
        super().takeBreathe()#prints all
        print("This is updated updated Im breathing..")
    

# p = Person()
# p.takeBreathe()

# e = Employee()
# e.takeBreathe()

# pgm = Programmer()
# pgm.takeBreathe()

pgm = Programmer()

#here its ur wish that we can run or not that constructors in
# derived classes by super().xxxxx()


#here two ways :-
'''
1) create a blank constructor in base class and a anormal one in the base class by 
multipuporse constructor mrthod and second is 
2) write super.__init__()'''