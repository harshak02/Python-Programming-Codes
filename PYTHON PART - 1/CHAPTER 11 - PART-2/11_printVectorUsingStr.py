class Vector :
    vec = []

    def __init__(self,vec1) :
        self.vec = vec1

    def __str__(self) :
        str1 = []
        strMain = ""#none shuld not be used
        for i in range (0,len(self.vec)) :
            if(i!=(len(self.vec)-1)) :
                str1.append(f"{self.vec[i]}a{i} + ")

            else :
                str1.append(f"{self.vec[i]}a{i}")#we can use str[:-1]
                
            strMain+=str1[i]#here we are adding so we need same datatypes

        return strMain

vec1 = Vector([1,4,7,90])

print(vec1)
