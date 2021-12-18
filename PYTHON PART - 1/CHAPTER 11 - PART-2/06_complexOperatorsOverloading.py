class Complex :
    real = None
    img = None
    result = None
    multiplication = None

    def __init__ (self,num1,num2) :

        self.real = num1
        self.img = num2

    def __add__ (self,comp2) :#done in C++ by this->(pointer)

        #for classes no need to write self.
        result.real = self.real + comp2.real
        result.img = self.img + comp2.img

        return result

    def __mul__ (self,comp2) :

        multiplication.real = ((self.real*comp2.real)-(self.img*comp2.img))
        multiplication.img = ((self.real*comp2.img)+(self.img*comp2.real))

        return multiplication

    def __str__(self) :

        if (self.img<0) :
            return f"The complex no. is : {self.real} - {-(self.img)}i"

        else :

            return f"The complex no. is : {self.real} + {self.img}i"

comp1 = Complex(2,3)
print(comp1)

comp2 = Complex(4,-55)
print(comp2)

comp3 = Complex(4,545)
print(comp3)

result = Complex(0,0)
multiplication = Complex(0,0)

result = comp1 + comp2 + comp3
multiplication = comp1*comp2*comp3

print(result)
print(multiplication)



# here we need to mention same name everywhere in operator overloading
# like in main function and also in the above class
