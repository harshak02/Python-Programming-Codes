from functools import reduce

def greater (num1,num2) :

    if(num1>num2) :
        return num1

    else :
        return num2

list1 = [1,2,3,4,5,6,7,8,9]

num = reduce(greater,list1)

print("The greatest is :",num)


