def rAndS(string,name) :

    newstr = string.replace(name,"")
    newstr = newstr.strip()
    print("Done!!")

    return newstr

string = "This is HarryBhai to all"

name = input("Enter the name to be removed :\n")

newstr = rAndS(string,name)
print(newstr)

