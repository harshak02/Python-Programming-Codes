for i in range (3) :

    try :

        f = open(f"{i+1}.txt","r")
        data = f.read()
        f.close()
        print(f"The file no. {i+1} is present") 
        print("The content is :",data)

    # except Exception as e :
    except FileNotFoundError as e :#the actual is FileNotFoundError
        print("Your file doesnt exist")
        print("for more information go thru :-")
        print("The error is :",e)

    except :
        print("An unknown error occured")

print("Done!!")


