class Employee :
    company = "Bharat Gas"
    salary = 1000
    bonus = 700
    totalSalary = None

    @property#getter also
    def totalSalary(self) :
        result = self.salary + self.bonus
        return result

emp = Employee()
emp.salary = 2000
print(emp.salary)
print(Employee.salary)#prints 1000 coz the above is instance change
print(emp.totalSalary)#instance change
# emp.totalSalary = 6444->it throws an error


