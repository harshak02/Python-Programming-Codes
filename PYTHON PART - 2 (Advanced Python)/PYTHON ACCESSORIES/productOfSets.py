# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

string1 = input()
list1 = list(map(int,string1.strip().split()))

string2 = input()
list2 = list(map(int,string2.strip().split()))


listFinal = product(list1,list2)

list1 = list(listFinal)

num = len(list1)
#this is used to convert list to string

for item in list1 :
    print(item,end=" ")
    
    
    
    
