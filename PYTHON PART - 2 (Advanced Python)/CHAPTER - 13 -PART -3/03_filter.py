def divisible (num) : 
    if (num%5==0) :
        return num

    else :
        pass

divisible = lambda num : (num%10==0)#overwrites the function
#if same arguments are there then it overwrites the befor one
#if different arguments then use a= None b =None.....method

list1 = [1,2,3,4,5,6,7,89,55,10]

list2 = []

list2 = list(filter(divisible,list1))

print(list2)
