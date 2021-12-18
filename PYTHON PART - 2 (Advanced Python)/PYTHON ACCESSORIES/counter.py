from collections import Counter

myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
list1 = Counter(myList)
print(list1)
#if we have like xxxx(list) then equate it to a number 
#in map only first we are writing the int and then list
#but in all other we need to write the list as 1st parameter and then func as 2nd
#and max if we have two parameters like map we need to datatype by list(map(x,x))
#but if list is the fisrt paramater then no need of list datatyping
#if it have only one parameter such as list like sum(list) The syntax is :
# num = sum(list)
#list1 = Counter(list1) or list1 = list1.__Counter__()

