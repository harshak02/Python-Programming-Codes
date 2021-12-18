class Error(Exception) :
    pass

class HarshaError(Error) :
    pass

while (True) :

    try :
        num1 = input("Enter the number 1 :\n")
        num2 = input("Enter the number 2 :\n")

        num1 = int(num1) 
        num2 = int(num2)

        if(num1 == 0 and num2 != 0) :
            raise HarshaError  

        else : 
            print(f"Your numbers are {num1} and {num2} and div is {num1/num2}")

    except HarshaError as z :
        print("Harsha Error Occured")
    
    except ZeroDivisionError as f :
        print("Number by zero not applicable")
        print(f)

    except ValueError as g :
        print("There is a value Error")
        print(g)

    except Exception as e :
        print("Enter the valid numbers")
        print("The actual error is :")
        print(e)

    except :
        print("Unknown Error")

    

