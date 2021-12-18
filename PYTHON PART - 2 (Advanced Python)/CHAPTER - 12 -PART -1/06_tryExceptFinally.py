# else is runs only when the try runs
#but 'finally' runs even when the pgm is exit

try :
    num = None
    num = input("Enter the number :")
    num = int(num)

    rec = 1/num
    print("The reciprocal is :",rec)

except ZeroDivisionError as e :
    print("division error occured")
    exit()#exits completely from the code

except Exception as e :
    print("unknown error occured")
    exit()

except :
    print("Error occured")
    exit()

finally :
    print("We have done with our code!! ->says finally")

print("We have done with our code!! ->says print")


