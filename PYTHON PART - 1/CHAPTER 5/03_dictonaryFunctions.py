mydict = {
    'a' : "apple",
    'b' : "ball",
    'c' : "cat",
    'd' : [1,2,3,4],
    'e' : {
        'f' : "fish",
        'g' : (5,6,7,8)
    },
    1 : 2

}

list1 = mydict.keys()#keys are the LHS and values are the RHS
print(list1)
print(type(mydict.keys()))#this type is class of dictionary to 
# convert it to pure list or tuple ->
list1 = list(mydict.keys())
print(list1)


list2 = mydict.values()
print(list2)
list2 =tuple(mydict.values())
print(list2)
print(type(list2))

print(mydict)

print(mydict.items())#gives the key and values in the respective
# tuples it is used in loops


