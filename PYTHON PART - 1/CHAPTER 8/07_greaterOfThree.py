def great (num1,num2,num3) :
    if (num1>= num2 and num1>= num3) :
        result = num1

    elif (num2>=num1 and num2>=num3) :
        result = num2

    else :
        result = num3

    return result


num1 = input("Enter the num1 :\n")
num1 = int(num1)

num2 = input("Enter the num2 :\n")
num2 = int(num2)

num3 = input("Enter the num3 :\n")
num3 = int(num3)

result = great(num1,num2,num3)

print("The greatest is : ",result)

