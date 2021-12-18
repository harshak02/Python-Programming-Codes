import calendar

#0 is Monday (the default), 6 is Sunday.

string = input()

list1 = list(map(int,string.strip().split()))

year = list1[2]

# print (calendar.TextCalendar(firstweekday=6).formatyear(year))

dayNumber = calendar.weekday(year, list1[1], list1[0])

print(dayNumber)
# listDay = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


# print(listDay[dayNumber])

