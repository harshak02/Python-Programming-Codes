class Vector :
    vec = []
    manVec = []
    #sum1 = None may or may not be writen better not write
    #coz its a class object
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



vec1 = Vector([1,2,3])
vec1.printData()

vec2 = Vector([4,5,6])
vec2.printData()

sum1 = Vector([0,0,0])

sum1 = vec1 + vec2
sum1.printData()

product = vec1*vec2
vec1.printData(65)

#ex :- self.sum.vec[1] is wrong because aldready sum is a class
#object
