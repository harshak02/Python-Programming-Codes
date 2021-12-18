hindict = {
    "aam"    :  "mango",
    "anar"   :  "promagranete",
    "sebh"   :  "apple",
    "tarbuz" :  "watermelon"
}

listimp = list(hindict.keys())

print("The options in the dictionary are :",listimp)
userinput = input("Enter the keyword\n")

# useroutput = hindict[userinput]
useroutput = hindict.get(userinput)

print("The meaning of",userinput,"is :",useroutput)
