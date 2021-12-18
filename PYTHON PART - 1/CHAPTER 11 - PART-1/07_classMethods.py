class Employee :
    company = "Camel"
    salary = 100
    location = "Delhi"

    def changeSalary (self,sal) :
        self.__class__.salary = sal#this is secondary method
        # self.salary = sal

    @classmethod
    def changeClassSalary (cls,sal) :#this is the perfect method
        cls.salary = sal

emp = Employee()
print(emp.salary)
emp.changeSalary(456)
# emp.changeClassSalary(455)
print(emp.salary)
print(Employee.salary)
# Employee.salary = 200
# print(Employee.salary)->this is one way but this is highly
# not recomendable
# emp1 = Employee()
# print(emp1.salary)





