class A :
    num1 = None

    def getData (self,val) :
        self.num1 = val

    def printData (self) :
        print("The num1 is :",self.num1)

class B(A) :
    num2 = None

    def __init__(self,val) :
        self.num2 = val

    def printData(self) :
        print("The num2 is :",self.num2)

a = A()
b = B(6)

a.getData(5)

a.printData()
b.printData()

#solved