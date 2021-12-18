line = "This is the code  depicting  double spaces"

doubleSpace = line.find("  ")
count = line.count("  ")
# print(type(doubleSpace))-> gives the datatype


if(doubleSpace==-1) : 
    print("There is no double space in string")

else : 
    print("There is a double space and the number of double spaces are :",count)




