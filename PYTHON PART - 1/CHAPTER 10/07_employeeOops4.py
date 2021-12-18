class Employee :
    salary = 100
    company = "Google"

    def getData(self) :
        print(self.salary) 
        print(self.company)


harry = Employee()
kavya = Employee()

harry.salary = 300
kavya.salary = 500

kavya.getData()
harry.getData()
#print(harry.address)#here address is not present (attribute)


