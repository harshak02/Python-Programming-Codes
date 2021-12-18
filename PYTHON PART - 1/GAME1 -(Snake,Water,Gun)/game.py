import random

def process (you,comp) :

    if (you=="s" and comp == "s") :
        result = 0

    elif (you=="s" and comp == "w") :
        result = 1

    elif (you=="s" and comp =="g") :
        result = -1

    elif (you=="w" and comp =="w") :
        result = 0

    elif (you=="w" and comp =="g") :
        result = 1

    elif (you=="w" and comp =="s") :
        result = -1

    elif (you=="g" and comp =="w") :
        result = -1

    elif (you=="g" and comp =="s") :
        result = 1

    else :
        result = 0

    return result

    



dict1 = {
    "s" : "for -> snake",
    "w" : "for -> water",
    "g" : "for -> gun"
}

print(list(dict1.items()))
you = input("Enter the selection from above list :\n")

comp = random.randint(1,3)


if(comp==1) :
    comp = "s"

elif(comp==2) :
    comp = "w"

else :
    comp ="g"

result = process (you,comp)


if(result==1) :
    print("Hurray! You won you chosen",you,"computer chosen",comp)

elif(result==-1) :
    print("Ouch! You lost you chosen",you,"computer chosen",comp)

else :
    print("The game is drawn! You both chosen",you)

print("Done!!")





