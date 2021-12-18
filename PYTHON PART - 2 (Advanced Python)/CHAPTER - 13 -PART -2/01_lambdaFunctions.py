# def func(num) :
#     result = num+5
#     return result

func = lambda num : num+5

square = lambda num : num*num

sum = lambda num1,num2,num3 : num1+num2+num3

num = input("Enter the number :\n")
num = int(num)

result = func(num)
print("The result of func is :",result)
print("The square is :",square(num))

num1 = input("Enter the number :\n")
num1 = int(num1)

num2 = input("Enter the number :\n")
num2 = int(num2)

num3 = input("Enter the number :\n")
num3 = int(num3)

print("The sum is :",sum(num1,num2,num3))



