num = input('Enter the number :\n')
num = int(num)

list1 = [str(num*i) for i in range(1,11)]#should be
#str for join method

print(list1)

verticalString ="\n".join(list1)

print(type(verticalString))#this is string

print(verticalString)
