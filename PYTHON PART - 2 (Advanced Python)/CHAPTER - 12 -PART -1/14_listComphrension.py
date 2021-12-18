list1 = [2,43,76,5,3,211,665,677,443,666]

list2 = []

for item in list1 :
    if (item%2==0) :
        list2.append(item)

print(list2)
#the above whole thing is done in single line :

list3 = [item for item in list1 if (item%2==0)] 

print(list3)

list4 = [item for item in list1 if(item>=600)]

print(list4)

#This is used when one list is prepared from other list
#by some conditions
