import textwrap#important

def wrap(string, max_width):

    listImp = textwrap.wrap(string,max_width)
    #listImp gives list

    mainString = "\n".join(listImp)
    
    return mainString

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
