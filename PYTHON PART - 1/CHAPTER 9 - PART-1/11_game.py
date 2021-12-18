def game (result) :
    return result


f = open("hisscore.txt","r")

data = f.read()
f.close()
# data = int(data)#not done this

result = game(98)


if(data=='') :# this should be done seperatly
    f = open("hisscore.txt","w") 
    f.write(str(result))#this should be string pakka
    f.close()


elif(result>=int(data)) :# here int should be written
    f = open("hisscore.txt","w") 
    f.write(str(result))#this should be string pakka
    f.close()


else :
    print("Score is too low")

print("Done!!")



