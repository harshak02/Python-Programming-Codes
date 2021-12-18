class Employee :
    company = "Bharat Gas"
    salary = 1000
    bonus = 700
    totalSalary = None

    @property
    def totalSalary(self) :
        result = self.salary + self.bonus
        return result

    @totalSalary.setter
    def totalSalary (self,val) :
        self.bonus = val - self.salary
        #we are changing the bonus keeping salary const.

emp = Employee()
print(emp.totalSalary)

emp.totalSalary = 3000#to solve this we use the setter
print(emp.salary)
print(emp.bonus)
print(emp.totalSalary)



