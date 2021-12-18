num = input("Enter the number :\n")
num = int(num)

print("")

for i in range(1,21,1) :
    mul = num*i
    # print(num,"X",i,"=",mul)
    print(f"{num} X {i} = {num*i}")# fstring

else :
    print("\nMultiplcation table printed")
