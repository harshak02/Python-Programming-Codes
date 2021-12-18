c = set()

c.add(18)
c.add("18")
print(c)


set1 = set()

set1.add(20)
set1.add(20.0)
set1.add("20")

num = len(set1)
print(num)

print(set1)# in python in sets the 20.0 and 20 are treated as same

