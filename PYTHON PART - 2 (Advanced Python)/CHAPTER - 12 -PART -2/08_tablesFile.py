num = input("Enter the number :\n")
num = int(num)

list1 = [1,2,3,4,5,6,7,8,9,10]

list2 = [(num*item) for item in list1 ]

f = open("Tables.txt","a")
f.write(str(list2))
f.close()

f = open("Tables.txt","a")
for i in range (1,11) :
    f.write(f"{num} X {i} = {list2[i-1]}\n")

f.write("*******************************\n")
f.close()

print(list2)
