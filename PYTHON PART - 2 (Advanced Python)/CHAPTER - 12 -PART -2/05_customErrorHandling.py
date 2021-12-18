class Error(Exception) :
    pass#this is mandatory :-
#created a cls named Error inherited from Exception(inbuilt)

class dobException (Error) :
    pass#this is the manual error class->
        #inherited from cls Error

year = input("Enter your Year of Birth :\n")
year = int(year)

age = 2021 - year 

try :
    if(age>=20 and age<=30) :
        print("Yes! you are eligible for Govt Exams")

    else :
        raise dobException#raise the exception named before

except dobException as e :
    print("Sorry! You are not eligible")

except Exception as e :
    print("Unknown error Occured")

except :
    print("Code crashed!")



