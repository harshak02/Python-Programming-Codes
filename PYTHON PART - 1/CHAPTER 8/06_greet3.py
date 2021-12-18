# def greet(name = "Sharanya") :
#     print("Good Morning! " + name)

def greet(name = None) :
    if(name!=None) :
        print("Good Morning!" + name)

    else :
        print("Good Morning!" + "Sharanya")

name1 = input("Enter your name :\n")

greet(name1)
greet()

print("\nDone")

