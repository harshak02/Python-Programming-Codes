from collections import deque

d = deque()
#similar to list
d.append(1)
d.appendleft(2)
d.append(2)
d.remove(2)
print(d)

d.extend("938373")
print(d)
num = d.pop()
print(d)
print(num)
#num1 = d.pop(2)
#print(num1)->wrong
num1 = d.popleft()
print(num1)

print(list(d))
p = list(d)
print(*p)#prints as a astring with spacses




