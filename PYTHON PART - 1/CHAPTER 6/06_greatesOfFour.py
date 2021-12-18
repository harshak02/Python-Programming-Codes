num1 = input("Enter the number 1 :\n")
num1 = int(num1)

num2 = input("Enter the number 2 :\n")
num2 = int(num2)

num3 = input("Enter the number 3 :\n")
num3 = int(num3)

num4 = input("Enter the number 4 :\n")
num4 = int(num4)

if(num1>=num2 and num1>=num3 and num1>=num4) :
    print("num1 is largest i.e :",num1)

elif(num2>=num3 and num2>=num1 and num2>=num4) :
    print("num2 is largest i.e :",num2)

elif(num3>=num2 and num3>=num1 and num3>=num4) :
    print("num3 is largest i.e :",num3)

else :
    print("num4 is largest i.e :",num4)

