def mutate_string(string, position, character):
    
    list1 = list(string)
    
    list1[position] = character
    
    newString = "".join(list1)
    
    return newString

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    # here * is not used coz only single char
    s_new = mutate_string(s, int(i), c)
    print(s_new)



    #Python strings can't be changed once they're created. However, you can use parts of the old string to make a new one.