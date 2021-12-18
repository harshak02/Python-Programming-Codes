class Employee :

    def setData(self,test) :
        self.company = test

    def getData(self) : 
        print(self.company)

kavya = Employee()

kavya.setData("google")
kavya.getData()

print("Done!!")

