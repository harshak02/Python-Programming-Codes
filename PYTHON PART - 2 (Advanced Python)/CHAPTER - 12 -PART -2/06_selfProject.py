import mselfProject_07

num1 = None
num2 = None

try :
    num1 = input("Enter the num1 :\n")
    num1 = int(num1)

    num2 = input("Enter the num2 :\n")
    num2 = int(num2)

    if(num1!=0 and num2!=0) :
        print(f"The fraction is {num1}/{num2}")

    elif(num1==0 and num2!=0) :
        print(f"The fraction is {num1}/{num2}")

    elif(num1==0 and num2==0) :
        raise mselfProject_07.NumError

    elif (num2==0) :
        raise mselfProject_07.DenError

    else :
        pass

except mselfProject_07.NumError as e:
    print("Error :The fraction is Not Defined")

except mselfProject_07.DenError as e:
    print("Error : The fraction is Infinte")

except Exception as e :
    print("Unknown error occured")

except :
    print("Error is out of range")

print("Done!!")
