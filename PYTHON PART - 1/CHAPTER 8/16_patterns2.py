def pattern (num) :
    for i in range(num) :
        for j in range(i+1) :
            print("*",end=" ")

        print(end="\n")



num = input("Enter the number :\n")
num = int(num)

pattern(num)
