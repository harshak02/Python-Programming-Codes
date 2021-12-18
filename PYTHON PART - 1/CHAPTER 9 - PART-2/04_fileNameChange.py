import os

f = open ("rename.txt","r")
data = f.read()
f.close()
os.remove("rename.txt")

f = open ("removed_by_python.txt","w")
f.write(data)
f.close()

print("Done!!")

