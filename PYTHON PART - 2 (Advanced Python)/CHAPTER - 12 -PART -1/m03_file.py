def greet(nam) :
    print(f"Good Morning!, {nam}")

def printData() :
    print("Hello!")

print(__name__)#this one runs 
if __name__ == "__main__" :

    nam = input("Enter the nam :\n")
    greet(nam)
    printData()#even though we have this only the required code runs






