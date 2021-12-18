def swap_case(s):
    
    mainString = ""
    
    for i in range (len(s)) :
        
        strTemp = None
        strTemp = s[i]
        
        bool1 = strTemp.islower()
        
        if(bool) :
        
            strTemp = strTemp.capitalize()#or
            strTemp = strTemp.upper()
            
        else :
            strTemp = strTemp.lower()
        
        mainString+=strTemp
        
    return mainString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    