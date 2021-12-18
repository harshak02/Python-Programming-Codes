f = open("logfile.txt","r") 
data = f.read()
f.close()

if("python" in data) :
    print("Yup Python is present")

else :
    print("Python is not present")


