def pattern (num) :

    print("*"*(num))

    for i in range(num-2) :
        print("*",end="")
        print(" "*(num-2),end="")
        print("*")

    print("*"*(num),end="")

num = input("Enter the number :\n")
num = int(num)

pattern(num)
