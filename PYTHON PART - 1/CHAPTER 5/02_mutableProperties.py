mydict = {
    'a' : "apple",
    'b' : "ball",
    'c' : "cat",
    'd' : [1,2,3,4],
    'e' : {
        'f' : "fish",
        'g' : (5,6,7,8)
    }
}

mydict['a'] = "aeroplane"
print(mydict['a'])

mydict['d'] = "array"
print(mydict)

mydict['e']['g'] = ("harsha",2,3,4)
print(mydict['e'])
