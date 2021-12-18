# \n,\t,\\ and \

string = "Harrybhai is a engineer.\nAnd he is graduated"
print(string)

string = "Harrybhai is a engineer.\tAnd he is graduated"
print(string)

string = "Harrybhai is a engineer.An\\d he is graduated"
print(string)#prints only single quote(backslash)

string = "Harrybhai is an CSE\"engineer.An\\d he is graduated"
print(string)#prints the apostrophe if we use single quote(\)

