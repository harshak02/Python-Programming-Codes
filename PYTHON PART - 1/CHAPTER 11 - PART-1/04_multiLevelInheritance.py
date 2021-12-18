class Person :
    country = "India"

    def takeBreathe(self) :
        print("Im breathing")

        # @staticmethod 
        # def takeBreathe2() :# write staticmethod outside the
        #     #function# coz we are using self here
        #     print("This is static breathe")

    @staticmethod 
    def takeBreathe2() :# write staticmethod outside the
        #function# coz we are using self here
        print("This is static breathe")

class Employee(Person) :
    company = "Honda"
    salary = 1000

    def getSalary(self) :
        print(f"The salary is {self.salary}")

    def takeBreathe(self):
        print("This is updated Im breathing..")


class Programmer(Employee) :
    company = "Fiverr"

    def getSalary(self):
        print("No salary to rogrammer")


    def takeBreathe(self):
        print("This is updated updated Im breathing..")
    

p = Person()
p.takeBreathe()
p.takeBreathe2()
e = Employee()
print(e.company)
e.takeBreathe()
pgm = Programmer()
print(pgm.company)
print(pgm.country)
pgm.takeBreathe()#gives the employee class function

Employee.takeBreathe2()
Programmer.takeBreathe2()


 