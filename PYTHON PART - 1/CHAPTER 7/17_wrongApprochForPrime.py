num = input("Enter the number :\n")
num = int(num)

temp = None

for i in range(2,num,1) :
    if (num%i==0) :
        print("The number",num,"is a composite")
        break

    else :
        temp = 1

if (temp==1) :
    print("The number",num,"is a prime")
