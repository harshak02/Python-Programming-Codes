try :
    print("Typing...")
    num = input("Enter the number :\n")
    num = int(num)
    rec = 1/num
    print("The reciprocal of",num,"is",rec)

except ZeroDivisionError as e :
    print("Division by zero is not defined")
    print("The error is :",e)

except :
    print("Unknown error occured")

else :
    print("The code runs without error")


print("Done!!")

#if try run"s succesfully then it goes to else
#here Exception is used for general errors