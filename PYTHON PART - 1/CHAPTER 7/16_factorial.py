num = input("Enter the number :\n")
num = int(num)
factorial = 1
for i in range(1,num+1) :

    factorial*=i

else :
    print("For loop invoked")

print(f"The factorial of {num} is = {factorial}")

