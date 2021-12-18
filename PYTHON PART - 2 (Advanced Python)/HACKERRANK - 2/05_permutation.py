# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

string = input()

list1 = string.strip().split()

list2 = list(permutations((list1[0]),int(list1[1])))

list2.sort()

for item in list2 :
    tempList = []
    tempList = list(item)
    stringNew = "".join(tempList)
    print(stringNew)