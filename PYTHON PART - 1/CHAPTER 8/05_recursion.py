def factorial(num1) :
    if(num1 == 0 or num1 == 1) :
        result = 1
    
    else :
        result = num1*factorial(num1-1)

    return result


num = input("Enter the number :\n")
num = int(num)

result = factorial(num)

print(f"The factorial of {num} is {result}")


#this recursion is used in algorithms

