class Person :
    country = "India"

    def takeBreathe(self) :
        print("Im breathing")


class Employee(Person) :
    company = "Honda"
    salary = 1000

    def getSalary(self) :
        print(f"The salary is {self.salary}")

    def takeBreathe(self):
        super().takeBreathe()
        print("This is updated Im breathing..")


class Programmer(Employee) :
    company = "Fiverr"

    def getSalary(self):
        print("No salary to rogrammer")


    def takeBreathe(self):
        super().takeBreathe()#prints all
        print("This is updated updated Im breathing..")
    

p = Person()
p.takeBreathe()

e = Employee()
e.takeBreathe()

pgm = Programmer()
pgm.takeBreathe()


