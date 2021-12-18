def div(a,b) :
    print(a/b)

def decorator(div) :

    def main(a,b) :
        if(a<b) :
            a,b = b,a

        return div(a,b)

    return main

div = decorator(div)

div(2,4)

