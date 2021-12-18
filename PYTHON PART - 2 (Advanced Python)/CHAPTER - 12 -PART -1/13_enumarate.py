list1 = [1,2,3,4,5,6,7,8,9,0]#can also contain different datatypes 

index = 0
for item in list1 :
    print(index,item)
    index+=1


#here the enumarate starts

for index,item in enumerate(list1) :#here always index should be first
    print("the item is :",item,"the index is :",index)



