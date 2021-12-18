# we cannot put list(mutable) or dictionary(mutable) in the set coz set is not changed
# a = set()
# a.add([4,5,6])
# print(a)

# b = set()
# b.add({4:5})
# print(b)

# we can put tuple(immutable) in the set coz set is not changed
c = set()
c.add((4,5,6))
c.add(4)
c.add(5)
print(c)

#sets are unordered and unindexed
#sets are not changable 

num = len(c)#this is the general syntax for len in all list,tup,set,dict.
print(num)

c.remove(5)
#c.remove(15)#throws error
print(c)

c.add(6)
print(c)

# c.pop()
#print(c)#removes randomly any value
print(c.pop())#gives the randomly removed value

# c.clear()
# print(c)->emptys the set

print(c.union({89,90}))# works only like this and works only here

# c.union(45,67)->wont work 
# # print(uni)->wont work
# print(c)

print(c.intersection({4}))# gives null set
print(c.intersection({6}))
print(c)#this one will be original

