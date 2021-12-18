list2 = [1,8,7,2,21,15]

list2.sort()
print(list2)#->this one will change the original one

# sorted_list =list2.sort()->this one gives none its a wrong practice
# print(sorted_list)

# list2 = list2.sort()->this one gives none its a wrong practice
# print(list2)
#this is the difference for strings and lists 
'''In list we no need to write the 
list2 = list2.sort() just if we write list2.sort() then also we can 
print the changed list and in strings we need to mention
like name = name.xxxx()'''

list2.reverse()
print(list2)

list2.append(45)#adds 8 at the last
print(list2)

list2.append(85)
print(list2)

list2.insert(0,544)
print(list2)
#the syntax is list2.insert(x,y) x -> the index of the adding one
#y -> is the number to be added

list2.pop(0)# removes the value at index mentioned in the the pop(*)
print(list2)

list2.remove(85)#removes the mentioned value
print(list2)

list2.append(45)
print(list2)

list2.remove(45)#removes only one 45 not all present in that
print(list2)

temp = list2[4]
list2[4] = list2[3]
list2[3] = temp

print(list2)

#in list realated functions dont use like list1 = list1.XXXX(xxxx)
