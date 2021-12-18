def convert(num) :
    result = 2.54*num
    return result


num = input("Enter the number :\n")
num = int(num)

result = convert(num)

print("The coverted centimeters is :",result,"\bcm")



