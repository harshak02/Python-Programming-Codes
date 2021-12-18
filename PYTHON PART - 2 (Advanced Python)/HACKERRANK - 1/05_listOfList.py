if __name__ == '__main__':
    
    num = int(input())
    
    mainList = []
    marksList = []
    
    for i in range(num):
        name = input()
        score = float(input())
        tempList = []
        tempList.append(name)
        tempList.append(score)
        marksList.append(score)
        mainList.append(tempList)
        
        
    setTemp = set(marksList)
    
    listTemp = list(setTemp)
    
    listTemp.sort()
    
    finalList = []
    
    for item in mainList :
        if(listTemp[1]==item[1]) :
            finalList.append(item)
            
        else :
            pass
        
    impList = []
        
    for item in finalList :
        impList.append(item[0])
        
    impList.sort()
    
    for item in impList :
        print(item)

