f = open("this.txt","r")
data1 = f.read()
f.close()

f = open("thiscopy.txt","r")
data2 = f.read()
f.close()

if(data1 == data2) :# we cannot use "is" here
    print("These files ar similar")

else :
    print("These are not similar")

print("Done!!")

