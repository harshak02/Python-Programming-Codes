def count_substring(string, sub_string):
    
    temp = sub_string[0]
    print(temp)
    count = 0
    
    for i in range (len(string)) :
        if(string[i]==temp) :
            tempImp = string[i:(i+len(sub_string))]
            print(tempImp)
            
            if(tempImp==sub_string) :
                count+=1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    