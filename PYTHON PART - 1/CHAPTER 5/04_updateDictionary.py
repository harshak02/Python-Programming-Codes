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

print(mydict)

updatedict = {
    "divya" : "friend",
    "harry" : (3,4,"Bhai"),
    'c'     : "caterpillar",
    'f'     : "frog"#adds a new key value(it means wont work)
}

mydict.update(updatedict)#updates permanantly for furthur opearations
print(mydict)

# print(mydict.update(updatedict))#this is not allowed
'''so for any of these list tuple and dictionary we need to
do it (applying functions) in the syntax like list.XXXX()
and then print(list) not in any other ways whereas in strings we 
need to do in other way so that we get the code correctly'''

print(mydict['d'])
print(type(mydict['d']))#this is aldready a list

mydict['d'] = list(mydict['d'])

mydict['d'].sort()#this one automatically changes the main one in
#dictionary also...

print(mydict)
print(mydict['d'])

'''Here if we use this->
 xxxxx = xxxx.()
 print(xxxxx) its like a change in the xerox copy but if
 
 xxxx.()
 print(xxxx) then it changes the original one and also this chnage
 is seen every where in code'''







