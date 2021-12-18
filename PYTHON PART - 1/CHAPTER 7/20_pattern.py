def pattern (num) :
    for i in range(num) :
        print(" "*(num-i-1),end="")
        print("*"*(2*i+1),end="")
        print(" "*(num-i-1))


num = input("Enter the number :\n")
num = int(num)

pattern(num)


