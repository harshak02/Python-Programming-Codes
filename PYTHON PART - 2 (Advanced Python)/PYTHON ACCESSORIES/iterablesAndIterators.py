#here list.__iter__() and iter(list)-> both are same

list1 = [1,2,3,4]
iterartor = iter(list1)

print(next(iterartor))
print(next(iterartor))
print(next(iterartor))
print(next(iterartor))
print(next(iterartor))#StopIteration