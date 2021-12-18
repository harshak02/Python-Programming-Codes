while (True) :

    print("Enter q to quit")
    num = input("Enter a number :\n")

    if (num=='q') :#mention this above only
        break

    else :
        try :
            num = int(num)#if wrong stops here
            print("trying...")

            if(num>=6) :
                print("The number is greater then 6")
                print(end="\n")

            else :
                print("The number is less than 6")
                print(end="\n")

        except Exception as e :
            print("The exception is :",e)
            print(end="\n")

print("Thanks for playing mini game!! Done!")


#specality is that even if exception comes the code runs 
#without crashing
