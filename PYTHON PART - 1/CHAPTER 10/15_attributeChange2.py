class Test :
    name = "Vicky"

    def printData(self) :
        print ("The name is :",self.name)
        
test1 = Test()
test2 = Test()

test1.name = "Harry"
test1.printData()
test2.printData()

#or
print(Test.name)# this benfit is there only in python
