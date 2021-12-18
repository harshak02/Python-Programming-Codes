# f = open("imptext.txt")-> 
# this default is read mode

# f = open("imptext.txt","r")
f = open("text.txt","r")

data = f.readline()#print single line
print(data,end="")

data = f.readline()#print single line
print(data)

# data = f.readline()#print single line
# print(data)

# data = f.readline()#print single line
# print(data)

f.close()






