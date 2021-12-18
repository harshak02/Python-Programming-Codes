try :
    num1 = input("Enter the number num1 :\n")
    num1 = int(num1)

    num2 = input("Enter the number num2 :\n")
    num2 = int(num2)

    print("Trying...")
    div = num1/num2
    print("The fraction is :",num1/num2)

except ZeroDivisionError as e :
    print("Infinite") 
    print("For more information go thru :-")
    print("The error is :",e)

except Exception as e :
    print("Error : Enter the valid number")

except :
    print("Error : An Unknown Error occured")


print("Done!!")

