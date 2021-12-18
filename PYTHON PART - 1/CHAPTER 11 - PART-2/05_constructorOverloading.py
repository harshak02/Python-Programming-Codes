class Base :
    num1 = 5

    def __init__(self=None,num=None) :

        if (self!=None and num!=None) :
            self.num1 = num

        elif (self!=None) :
            pass

        else :
            pass


class Der (Base):
    num2 = 6

    def getData (self,val) :
        self.num2 = val

    def printData (self) :
        print("The num1 is :",self.num1)
        print("The num2 is :",self.num2)

b = Base(4)
d = Der()
# d.getData(9)
d.num2 = 9
d.printData()

print("Done!!")
