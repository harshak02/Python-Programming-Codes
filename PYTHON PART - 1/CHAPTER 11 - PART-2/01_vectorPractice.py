class Vector :
    x = None
    y = None#->this plays the imp role for derived cls

    def __init__(self,num1,num2) :
        self.x = num1
        self.y = num2

    # def printData(self) :
    #     print(f"The vector is : {self.x}i + {self.y}j")

    def __str__(self) :
        return f"The vector is : {self.x}i + {self.y}j"




class VectorDer(Vector) :
    #instance attributes are not carried here only class
    #attributes are carried like x = None but x can't inherit
    # value to derived class y __init__()
    z = None

    def __init__(self,num1,num2,num3) :
        super().__init__(num1,num2)
        self.z = num3

    # def printData(self) :
    #     print(f"The vector is : {self.x}i + {self.y}j +{self.z}k")

    def __str__(self) :
        return f"The vector is : {self.x}i + {self.y}j + {self.z}k"

vec1 = Vector(4,5)
# vec1.printData()
print(vec1)
vec2 = VectorDer(4,5,6)
# vec2.printData()
print(vec2)
