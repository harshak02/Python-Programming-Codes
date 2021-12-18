num = input("Enter the number :\n")
num = int(num)

prime = True

for i in range(2,num,1) :
    if (num%i==0) :
        prime = False
        break

if (prime) :
    print("The number",num,"is a prime")

else :
    print("The number",num,"is a composite")

print("\nDone! :-)")
