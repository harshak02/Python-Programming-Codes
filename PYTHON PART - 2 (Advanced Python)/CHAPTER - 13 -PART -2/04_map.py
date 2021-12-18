def square (x) :
    result = x*x
    return result

list1 = [1,2,3,4]

list2 = []

for item in list1 :
    list2.append(item*item)

print(list2)

list3 = list(map(square,list1))#imp #can be a lamda function also

print(list3)


