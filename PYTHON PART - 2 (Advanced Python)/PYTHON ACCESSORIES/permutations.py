# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

string = input()
list1 = string.strip().split()

list1[0] = list(list1[0])
list1[0].sort()

list2 = list(permutations((list1[0]),int(list1[1])))


for item in list2 :
    tempList = []
    tempList = list(item)
    stringNew = "".join(tempList)
    print(stringNew)


