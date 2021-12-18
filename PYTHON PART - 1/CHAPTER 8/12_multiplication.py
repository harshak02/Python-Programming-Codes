def mult (num) :
    for i in range (1,21,1) :
        mul = num*i
        print(f"{num} X {i} = {mul}")



num = input("Enter the number :\n")
num = int(num)

mult(num)

print("\nDone")
