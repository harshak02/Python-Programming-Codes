class Vector :
    vec = []
    manVec = []
    addlen = None
    product = None

    def __init__(self,vectemp) :

        self.vec = vectemp

    def __add__(self,vec2) :

        for i in range (0,3) :
            sum1.vec[i] = self.vec[i] + vec2.vec[i]

        return sum1


    def __mul__(self,vec2) :

        for i in range (0,3) :
            self.manVec.append(self.vec[i]*vec2.vec[i])

        self.product = sum(self.manVec)

        return self.product


    def printData (self,num=None) :
        if(num!=None) :
            print("The dot product is :",self.product)

        else :
            print(f"The vector is : {self.vec[0]}i +{self.vec[1]}j +{self.vec[2]}k")

    def addCheck (self) :
        temp = len(vec1.vec)

        temp2 = self.vec.count(0) 
        Vector.addlen = len(self.vec) - temp2

        if(Vector.addlen<temp) :
            print("Thereom is wrong with :",Vector.addlen)

        else :
            print("thereom is correct with :",Vector.addlen)



vec1 = Vector([1,2,3])
vec1.printData()

vec2 = Vector([4,-2,6])
vec2.printData()

sum1 = Vector([0,0,0])

sum1 = vec1 + vec2
sum1.printData()
sum1.addCheck()

product = vec1*vec2
vec1.printData(65)

