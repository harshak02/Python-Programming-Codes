f = open("poems.txt","rt")
data = f.read()

if("twinkle" in data) :
    print("Yeah the word 'twinkle' is present")

else :
    print("Im sorry no word is present")

print("\nDone!!")

