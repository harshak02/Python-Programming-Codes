num = input("Enter the number :\n")
num = int(num)

list1 = []
for i in range(1,11) :
    list2 = []
    list2.append(num*i)
    list1.append(list2)


print(list1)

print('Done')
