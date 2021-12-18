f = open("logfile.txt","r") 
data = f.read()
f.close()

f = open("logfile.txt","r")

for i in range (500) :
    data = f.readline()
    if("python" in data) :
        print("Yup python is there in",i+1,"th line")

        break

print("Done!!")
 