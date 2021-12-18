list1 = ["shubam","harry","kavya","Sruthi"]
num = len(list1)

for i in range(num) :
    if(not(list1[i][0]=='s' or list1[i][0]=='S')) :
        pass

    if(list1[i][0]=='s' or list1[i][0]=='S') :
        print("Greetings to you :",list1[i])

else :
    print("\nDone!")



