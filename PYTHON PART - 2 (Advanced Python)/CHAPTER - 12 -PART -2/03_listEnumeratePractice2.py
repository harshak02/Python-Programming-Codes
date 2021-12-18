num = input("Enter the number :\n")
num = int(num)

list1 = [1,2,3,4,5,6,7,8,9,10]

list2 = [(num*item) for item in list1 ]

print(list2)
