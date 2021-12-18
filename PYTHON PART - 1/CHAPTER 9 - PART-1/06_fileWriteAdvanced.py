f = open("writesample.txt","w")
f.write("hello im harsha\n")
f.write("Im learning Python\n")
f.write("hello im harsha\n")
f.write("Im learning Python")
f.close()# once we close the file and again if we
#try to write anything the data will be erased
#instead use append to attach at last..

f = open("writesample.txt","w")
f.write("hello im harsha\n")
f.write("Im learning Python\n")
f.write("hello im harsha\n")
f.write("Im learning Python")
f.close()
# only writes the hello->to Python only 2 times
