list1 = [2,4,6,8,10,12,14,16,18,20]

list2 = [item for item in list1 if (item==list1[2] or item==list1[4] or item==list1[6])]

print(list2)

list3 = [1,2,3,4,5,6,7,8,9,10] 

list4 = []

for index,item in enumerate(list3) :
    if (index==2 or index==4 or index==6) :
        list4.append(item) 
        print(index,item)

print(list4)

