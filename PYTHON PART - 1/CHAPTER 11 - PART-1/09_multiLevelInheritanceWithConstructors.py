class A :
    num1 = None

    def __init__(self,a) :
        self.num1 = a


class B(A) :
    num2 = None

    def __init__(self,a,b) :
        super().__init__(a)
        self.num2 = b

class C(B) :

    num3 = None

    def __init__(self,a,b,c) :
        super().__init__(a,b)#here no need to use self
        self.num3 = c

    def printData(self) :
        print(self.num1)
        print(self.num2)
        print(self.num3)

c = C(4,5,6)
c.printData()
