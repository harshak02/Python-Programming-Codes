num = input("Enter the number please :\n")

try :
    print("Trying...")
    num = int(num) 
    rec = 1/num
    print(f"The reciprocal of {num} is {rec}")

except ZeroDivisionError as e :
    print("Error : ")    
    print("Division by zero is not allowed")

except ValueError as e :
    print("Error : ")
    print("Enter the number....not a string")

except :
    print("An unknown error occured!")


print("Thanks for using the code!")

#if and else are same like try and except 