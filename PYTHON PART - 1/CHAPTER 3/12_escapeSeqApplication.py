letter = "Dear Harry! This Python Course is nice. Thanks! :-)"

#making it neat(formating document by using escape seq char's)

letter = letter.replace("Harry!","Harry!\n")
letter = letter.replace(" This","\tThis")
letter = letter.replace(" Thanks!","\n\tThanks!")

print(letter)

formated_letter = "Dear Harry!\n\t This Python Course is nice.\n\t Thanks! :-)"
print(formated_letter)

