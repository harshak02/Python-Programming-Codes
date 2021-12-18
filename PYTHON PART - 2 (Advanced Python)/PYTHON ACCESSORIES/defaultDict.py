from collections import defaultdict

myDict = defaultdict(list)

myDict["Hello"].append("world")
myDict["Roll No"].append((1,2,3,4,5))

list1 = list(myDict.keys())
print(list1)
list1 = myDict.values()#original is dict type
print(list1)
print(myDict)

