def greater_Than_5(num) :
    if (num>5) :
        return True#this is imp

    else :
        return False

def di_Greater_Than_5(num) :
    if (num>5) :
        return num#this is imp

    else :
        pass

g10 = lambda num : (num>5)#no need to write if

list1 = [1,67,89,0,2,3,7,8,99,45]

list2 = list(filter(greater_Than_5,list1))
print(list2)#dont prints None

list3 = list(map(di_Greater_Than_5,list1))
print(list3)#prints None if value is not there

list4 = list(filter(g10,list1))
print(list4)
