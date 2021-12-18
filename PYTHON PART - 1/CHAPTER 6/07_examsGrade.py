marks1 = input("Enter the marks in suject 1 :\n")
marks1 = int(marks1)

marks2 = input("Enter the marks in suject 2 :\n")
marks2 = int(marks2)

marks3 = input("Enter the marks in suject 3 :\n")
marks3 = int(marks3)

list1 = [marks1,marks2,marks3]

percent = sum(list1)/3# sum syntax
percent = int(percent)

if(marks1<33 or marks2<33 or marks3<33 or percent<40) :
    print("You are fail and your percentage is :",percent)

else :
    print("You passed and your percentage is :",percent)

