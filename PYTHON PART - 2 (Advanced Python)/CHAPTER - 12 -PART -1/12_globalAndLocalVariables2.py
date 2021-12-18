a = 54 

def func1() :
    global a #this uses the global varibale and
    #we can change the global variable
    a = 78
    print("the value of a in 1st case :",a)


func1()
print("the value of a in 2nd case :",a)
a = 89
print("the value of a in 3rd case :",a)
