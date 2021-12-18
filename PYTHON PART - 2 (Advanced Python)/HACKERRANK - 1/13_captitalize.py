import os

def solve(s):
    
    for i in range (len(s)) :
        if(i==0) :
            temp1 = s[i]
            tempImp1 = temp1.capitalize()
            string = s.replace(temp1,tempImp1)

        elif(i=="") :
            for j in range (100) :
                s[i+j]!=""
                temp2 = s[i+j]
                tempImp2 = temp2.capitalize()
                stringImp = string.replace(temp2,tempImp2)

        else :
            pass

    return stringImp
        

if __name__ == '__main__':


    s = input()

    result = solve(s)

    print(result)
