mydict = {
    'a' : "apple",
    'b' : "ball",
    'c' : "cat",
    'd' : [2,4,3,1],
    'e' : {
        'f' : "fish",
        'g' : (5,6,7,8)
    },
    1 : 2

}

print(mydict.get("d"))
print("*****************")
print(mydict["d"])

print(mydict.get("k"))#gives none
# print("*****************")
# print(mydict["k"])#throws error

'''if we use the [sq brackets] then compulsorily the key should be
prsent in the code in any situation if not it throws error'''
