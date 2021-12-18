# changing class attribute

class Employee :
    company = "google"

    def printData (self) :
        print(self.company)

harry = Employee()
kavya = Employee()

harry.printData()
kavya.printData()

#changing data ->
Employee.company = "Facebook"#this changes all the objects

harry.printData()
kavya.printData()

