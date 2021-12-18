class Complex :
    real = None
    img = None
    result = None

    def __init__(self,real1,img1) :
        self.real = real1
        self.img = img1


    def __add__(self,comp2) :
        result.real = self.real + comp2.real
        result.img = self.img + comp2.img
        return result

    def __str__(self) :
        return f"The complex no. is : {self.real} +{self.img}i"

comp1 = Complex(2,3)
print(comp1)
comp2 = Complex(4,5)
print(comp2)
comp3 = Complex(6,7)
print(comp3)

result = Complex(0,0)
result = comp1 + comp2 +comp3#we can use for any no. of times
print(result)


