def pattern (num) :
    for i in range(num) :
        for j in range(num-i) :
            print("*",end=" ")

        print(end="\n")



num = input("Enter the number :\n")
num = int(num)

pattern(num)
