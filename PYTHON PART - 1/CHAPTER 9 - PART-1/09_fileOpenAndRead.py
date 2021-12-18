f = open("test.txt","w")
f.write("You are talented\n")
f.write("Your are good")
f.close()

f = open("test.txt","r+")#default t
#here the r+ means reading + writing so here writing(appending)
#will work as append it wont erase the previosu data 
data = f.read()
f.write("heelooooooo")
print(data)
f.close()



