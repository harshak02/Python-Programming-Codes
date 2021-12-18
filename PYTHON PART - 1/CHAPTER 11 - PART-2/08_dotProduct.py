class Vector :
    x = None
    y = None
    z = None
    #sum = None->dont mention here coz its a class object
    #even mentioned no problem
    product = None
    product1 = None

    def __init__(self,num1,num2,num3) :

        self.x = num1
        self.y = num2
        self.z = num3

    def __add__(self,vec2) :

        sum.x = self.x + vec2.x
        sum.y = self.y + vec2.y
        sum.z = self.z + vec2.z

        return sum


    def __mul__(self,vec2) :

        self.product = (self.x*vec2.x)+(self.y*vec2.y)+(self.z*vec2.z)
        # self.product1 = self.product# assigned only in vec1 object
        return self.product

    # def __str__ (self=None,num=None) :#we cant overload this

    #     if(self!=None and num!=None) :
    #         return f"The dot product is {num}"

    #     elif (self!=None) :
    #         return f"The vector is : {self.x}i +{self.y}j +{self.z}k"

    #     else :
    #         pass

    def printData (self,num=None) :
        if(num!=None) :
            print("The dot product is :",self.product)

        else :
            print(f"The vector is : {self.x}i +{self.y}j +{self.z}k")



vec1 = Vector(1,2,3)
vec1.printData()
# print(vec1)
vec2 = Vector(4,5,6)
vec2.printData()
# print(vec2)
sum = Vector(0,0,0)

sum = vec1 + vec2
sum.printData()
# print(sum)

product = vec1*vec2
#sum.printData(product)
vec1.printData(65)#use vec1.printData or pass product and pass
# this 
# print(67)

print("Done!!")


#for constructor overloading functions include in class itself