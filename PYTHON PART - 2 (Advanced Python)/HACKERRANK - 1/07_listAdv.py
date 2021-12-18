if __name__ == '__main__':
    N = int(input())
    
    mainList = []
    
    for i in range (N) :
        
        tempList = input().strip().split()#->this is list
        #gives the list which contain all strings only no int or float
        
        if(len(tempList)== 3) :
            
            mainList.insert(int(tempList[1]),int(tempList[2]))
            
        elif(len(tempList)== 2) :
            if(tempList[0]=="remove") :
                mainList.remove(int(tempList[1]))
             
            else :
                mainList.append(int(tempList[1]))
                
        else :
            if(tempList[0]=="print") :
                print(mainList)
                
            elif(tempList[0]=="pop") :
                mainList.pop()
                
            elif(tempList[0]=="sort") :
                mainList.sort()
                
            else :
                mainList.reverse()
                