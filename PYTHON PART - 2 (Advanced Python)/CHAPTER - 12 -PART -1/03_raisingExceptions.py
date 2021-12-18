def increment (num) :
    try :
        result = num+1
        return result

    except : 
        raise ValueError("This is an error")

num2 = increment("hj")
print(num2)


#creates an exception
