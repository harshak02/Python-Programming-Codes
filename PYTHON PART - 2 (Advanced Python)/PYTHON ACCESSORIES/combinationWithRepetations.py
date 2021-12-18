# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

str1,num = input().strip().split()
list1 = list(str1)
list1.sort()
listImp = []


listImp = list(combinations_with_replacement(list1,int(num)))

for item in listImp :
    item = list(item)
    print("".join(item))
    

    
