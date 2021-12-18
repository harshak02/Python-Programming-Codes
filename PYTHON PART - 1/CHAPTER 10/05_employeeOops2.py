# changing class attribute

class Employee :
    company = "google"# this is class attribute

    def printData (self) :
        print(self.company)

harry = Employee()
rajini = Employee()
harry.printData()
print(rajini.company)


harry.company = "Facebook"#this is instance attribute
#this one also changes
harry.printData()
rajini.printData()


