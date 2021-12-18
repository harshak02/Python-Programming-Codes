class A :
    num1 = 8 

    def __init__(self = None,val1 = None) :
        if (self!=None and val1!=None) :
            self.num1 = val1

        else :
            pass
        

    def printData(self) :
        print("The num1 is :",self.num1)


class B(A) :
    num2 = None 

    def getData (self,val2) :
        self.num2 = val2

    def printData(self) :
        print("The num2 is :",self.num2)
        print("The num1 is :",self.num1)


a = A(4)
b = B()

b.getData(5)
a.printData()
b.printData()

'''we need to use blank constructors only if there is constructor in base 
class and not there in derived cls

we need to use blank contsructors in all other cases or else use super
method''' 

