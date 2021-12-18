list1 = ["brutal","waste","rascal"]

f = open("censored.txt","r")
data = f.read()
f.close()

datanew1 = data.replace(list1[2],"******")
datanew2 = datanew1.replace(list1[0],"******")
datanew3 = datanew2.replace(list1[1],"*****")

f = open("censored.txt","w")
f.write(datanew3)
f.close()

print("Done!!")
