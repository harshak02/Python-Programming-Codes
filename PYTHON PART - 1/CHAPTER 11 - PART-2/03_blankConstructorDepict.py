class Base :
    num1 = 9

    def __init__(self,val) :
        self.num1 = val

    def __init__(self) :
        pass#only down constructor is taken by python
#dont use this

class Der(Base) :
    num2 = None

    def setValue (self,val2) :
        self.num2 = val2

    def printData(self) :
        print(f"The num2 is : {self.num2}")
        print(f"The num1 is : {self.num1}")
        print(f"{Base.num1}")



d = Der()#in c++ no need to use brackets
d.setValue(4)
d.printData()


#here the blank constructor is required only in the case of