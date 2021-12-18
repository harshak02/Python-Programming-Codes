def sum (num1=None,num2=None,num3=None) :#this
    #is the proccess
    if(num1!=None and num2!=None and num3!=None) :
        result = num1+num2+num3

    elif(num1!=None and num2!=None) :
        result = num1+num2

    elif(num1!=None) :
        result = num1

    else :
        result = None

    return result

s = sum(4,5)
print(f"The sum is : {s}")

