import numpy as np

#1D array means 1 axis 
#2d array means 2 axis i.e :-
#axis0 for vertical and axis1 for horizontal

list1 = [[1,2,3],[4,5,6],[7,1,0]]

listAxis = np.array(list1)
print(listAxis)

sumrows = listAxis.sum(axis=0)
print("The sum of the rows is :-",sumrows)

sumcols = listAxis.sum(axis=1)
print("The sum of the cols is :-",sumcols)


transpose = listAxis.T
print(transpose)

flat = listAxis.flat#imp

for item in flat :
    print(item)

print(listAxis.ndim)#gives the dim of array
#gives 2

print(listAxis.nbytes)#gives the bytes consumed of array



