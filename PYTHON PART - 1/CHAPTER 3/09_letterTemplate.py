name = input("Enter your name please\n")
date = input("Enter your date please\n")

letter = '''Dear <name>
     You are selected! :-)
     dt :- <date>'''

letter = letter.replace("<name>",name)
letter = letter.replace("<date>",date)

print(letter)

# print(letter.replace("<name>",name),letter.replace("<date>",date))
# the above one wont workout...prints two times the template



