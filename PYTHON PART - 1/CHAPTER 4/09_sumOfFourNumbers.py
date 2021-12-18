list = []

num1 = input("Enter the number 1\n")
num1 = int(num1)
list.append(num1)

num2 = input("Enter the number 2\n")
num2 = int(num2)
list.append(num2)

num3 = input("Enter the number 3\n")
num3 = int(num3)
list.append(num3)

num4 = input("Enter the number 4\n")
num4 = int(num4)
list.append(num4)

print(list)

# sum = num1 +num2 +num3 +num4
# sum = list[0] + list[1] + list[2] + list[3]

int = sum(list)
# print("The sum of the numbers in the list is =",sum)
print("The sum of the numbers in the list is =",int)

#for list realeted pls use like num = list.count(XXX) likwise other than that use only list.xxxx(xx)


