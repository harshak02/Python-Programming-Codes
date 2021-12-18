def sum(num) :
    if(num==1) :
        result = 1
    
    else :
        result = num + sum(num-1)

    return result


num1 = input("Enter the num1 :\n")
num1 = int(num1)

result = sum(num1)

print("The sum of",num1,"numbers is",result)

