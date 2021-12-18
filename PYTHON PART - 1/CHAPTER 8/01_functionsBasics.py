def percent(marks) :
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400*100)
    return p

list1 = [90,93,99,97]
percentage1 = percent(list1)
print(percentage1)

list2 = [86,100,98,95]
percentage2 = percent(list2)
print(percentage2)
