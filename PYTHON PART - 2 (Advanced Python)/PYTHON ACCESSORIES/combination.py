from itertools import combinations

list1 = [1,2,3,4]

string1 = "1234"

listComb1 = list(combinations(list1,2))
#the combination(list,num) : num indicates the no of elemets
#in subsets of combination#the subsets are tuples

listComb2 = list(combinations(string1,3))

print(listComb1)
print(listComb2)

