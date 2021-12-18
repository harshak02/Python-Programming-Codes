import math

class Calculator :
    num = None
    result1 = None
    result2 = None
    result3 = None

    def __init__(self,test) :
        self.num = test

    def maths(self) :
        self.result1 = self.num*self.num
        self.result2 = self.num*self.num*self.num
        self.result3 = math.sqrt(self.num)#write math.xxxx for libraryFiles

    def printData(self) :
        print("The square of",self.num,"is",self.result1)
        print("The cube of",self.num,"is",self.result2)
        print("the squareRoot of",self.num,"is",self.result3)


num1 = input("Enter the number :\n")
num1 = int(num1)

number = Calculator(num1)

number.maths()
number.printData()

print("Done!!")

'''we can also use the syntax for power with out any import
of library  (self.num **2)-> power 2
(self.num **0.5)-> sqr root'''
