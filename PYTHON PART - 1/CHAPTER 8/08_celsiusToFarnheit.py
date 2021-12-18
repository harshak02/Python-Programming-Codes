def convert (num) :
    result = 1.8*num + 32
    return result


temp = input("Enter the temperature in *C :\n")
temp = int(temp)

result = convert(temp)

print("The farenhiet for",temp,"is",result)



