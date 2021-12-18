name = "HarryBhai"
print(name[4])
print(type(name[4]))

#name[3] = "k" this one wont work in C
#in C k can be written as 'k' but in python we can also write as "k"

print(name[0:4])#here 0 is included and 4 is excluded
print(name[1:3])#here 1 is included and 3 is excluded
print(name[:4])#similar to first case
print(name[0:])#print whole string

#negative indices
print(name[-4:-1])
# print(name[-1:-4])#this is wrong first put magnitude higher number
