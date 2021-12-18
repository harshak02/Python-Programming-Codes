with open ("this.txt","r") as f :
    data = f.read()


with open ("thiscopy.txt","w") as f :
    f.write(data)

print("Done!!")
