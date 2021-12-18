# Enter your code here. Read input from STDIN. Print output to STDOUT

num1 = input()
num1 = int(num1)

string1 = input()
list1 = string1.strip().split()

list11 = list(map(int,list1))

num2 = input()
num2 = int(num2)

string2 = input()
list2 = string2.strip().split()

list22 = list(map(int,list2))

set1 = set(list11)
set2 = set(list22)

set3 = set1.union(set2)#this is a set

print(len(set3))



'''
>>> s = set("Hacker")
>>> print s.union("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(set(['R', 'a', 'n', 'k']))
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(['R', 'a', 'n', 'k'])
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(enumerate(['R', 'a', 'n', 'k']))
set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

>>> print s.union({"Rank":1})
set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

>>> s | set("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])
'''
