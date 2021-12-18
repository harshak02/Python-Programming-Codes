f = open("donkey.txt","r")
data = f.read()
f.close()

datanew = data.replace("donkey","######")

f = open("donkey.txt","w")
f.write(datanew)
f.close()

print("Done!!")

