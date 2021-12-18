text = input("Enter the text :\n")

if(text in "subscribe now") :
    spam = True#same like function

elif(text in "Get money") :
    spam = True

elif(text in "click this") :
    spam = True

else :
    spam = False 

if(spam) :
    print("This is a spam")

else :
    print("This is not a spam")
      