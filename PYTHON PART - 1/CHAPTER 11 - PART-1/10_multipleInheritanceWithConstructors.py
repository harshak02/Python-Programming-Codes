class A :
    num1 = None

    def __init__(self,a) :
        self.num1 = a
        print("A Invoked")

class B :
    num2 = None

    def __init__(self,b) :
        self.num2 = b
        print("B Invoked")

class C(A,B) :
    num3 = None 

    def __init__(self,a,b,c) :
        A.__init__(self,a)
        B.__init__(self,b)# here we need to use self
        #coz we are explicitly calling constructor 
        self.num3 = c
        print("C Invoked")

    def printData(self) :
        print(self.num1)
        print(self.num2)   
        print(self.num3)

c = C(4,5,6)
c.printData()
