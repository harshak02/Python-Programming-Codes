f = open("writesample.txt","+")
f.write("hello im harsha\n")
f.write("Im learning Python\n")
f.write("hello im harsha\n")
f.write("Im learning Python")
data = f.read()#throws an error
# Must have exactly one of create/read/write/append mode and at most one 
f.close()

print(data)

