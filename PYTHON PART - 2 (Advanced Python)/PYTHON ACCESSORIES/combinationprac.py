# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

string,num = input().strip().split()
# list1 = list(string)
# list1.sort()
# string = "".join(list1)
# print(string)

num = int(num)

listNew = []

for i in range (1,num+1) :

    list1 = list(combinations(string,i))
    
    for item in list1 :
        strNew = ""
        for i in range(len(item)) :
            strNew+=(item[i])
            
        
        listNew.append(strNew)
        
        
for item in listNew :
    print(item)
