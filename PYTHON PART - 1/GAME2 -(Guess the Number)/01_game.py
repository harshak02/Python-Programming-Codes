import random 

number_of_guesses = 1#here one should be taken coz
#the else will not increse the number of guesses 
guess = None
num = random.randint(1,99)#here both are included

guess = input("Enter the number :\n")
guess = int(guess)#we can put this even inside the loop coz guess is intially None

while (guess!=num) :

    if (guess>num) :
        print("Lower number please!")
        guess = input()#this is important
        guess = int(guess)        

    elif (guess<num) :
        print("Higher number please")
        guess = input()
        guess = int(guess) 

    else :
        pass 

    

    number_of_guesses+=1

else :
    print("Hurray your guess is correct!")
    print("The number is :",num)
    print("the number of guesses is :",number_of_guesses)

print("Done!!")

f = open("highScore.txt","r")

data = f.read()
f.close()

if(data is None) :
    f = open("highscore.txt","w")
    f.write(str(number_of_guesses))
    f.close()

else :

    data = int(data)

    if(data>number_of_guesses) :
        f = open("highscore.txt","w")
        f.write(str(number_of_guesses))
        f.close()

    else :
        pass


