# if we use double underscorer then we call it as dunder method

class Number :
    num = None

    def __init__(self,num) :
        self.num = num

    def __add__(self,n2) :#one should be
    # self and other should be pretended as self of other class
        print("The addition is in process")
        result = self.num + n2.num
        return result#this is crct

    def __mul__(self,n2) :
        print("Lets Multiply!")
        result1 = self.num * n2.num
        return result1

# def __add__(n1,n2) :
#     print("Lets Add!")->this should not be written outside
#     result = n1.num + n2.num
#     return result

n1 = Number(4)
n2 = Number(5)

sum = n1+n2
product = n1*n2

print("The sum of the two numbers is :",sum)
print("The product of the two numbers is :",product)

#imp :- conc on the ouput order :-) once its imp
