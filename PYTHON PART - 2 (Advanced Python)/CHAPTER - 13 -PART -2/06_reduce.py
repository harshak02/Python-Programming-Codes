from functools import reduce 

sum = lambda a,b : a+b

list1 = [1,2,3,4,5,6]

val = reduce(sum,list1)
print(val)
