f = open("wipe.txt","r") 
data = f.read()
f.close()

datanew = data.replace(data,"") #Or
data = ""

f = open("wipe.txt","w") 
f.write(datanew)
f.close()

print("Done!!")

