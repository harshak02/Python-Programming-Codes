def sum(num1,num2) :
    result = num1 + num2
    return result

num1 = input("Enter the number 1 :\n")
num1 = int(num1)

num2 = input("Enter the number 2 :\n")
num2 = int(num2)

result = sum(num1,num2)

print("The sum of",num1,"and",num2,"is",result)
