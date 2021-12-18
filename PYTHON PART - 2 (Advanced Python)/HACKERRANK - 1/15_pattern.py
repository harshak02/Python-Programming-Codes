string = input()

list1 = string.strip().split()

list2 = list(map(int,list1))

num1 = list2[0]
num2 = list2[1]

list3 = []

for i in range (int((num1/2)+1)) :#int is must if we use division
    
    if(i==((num1-1)/2)) :
        print ("WELCOME".center(num2,"-"))
    
    elif(i<=int(num1-1)/2) :
        
        tempStr = ""
        
        temp1 = int((((num2 - (2*i+1))/2)-(2*i+1))) 
        temp2 = int(((2*i)+1))

        print("-"*(temp1),end="")
        tempStr = "-"*(temp1)
        print(".|."*(temp2),end="")
        tempStr +=".|."*(temp2)
        print("-"*(temp1),end="")
        tempStr += "-"*(temp1)
        print(end="\n")
        list3.append(tempStr)

        
        

list3.reverse()

for item in list3 :
    print(item)
    
    

        
        
