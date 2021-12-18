#here array.xxxx means attribute and array.xxxx() means method or function

import numpy as np 

one = np.array([1,2,345,6,7,888])
ar = np.array([[1,2,3],[4,5,6],[7,1,0]])

print(one.argmax())#gives the arg of the max value of array
print(one.argmin())#gives the arg of the min value of array
print(one.argsort())#gives order of sorted orders


print(ar.argmax(axis=0))
print(ar.argmax(axis=1))
print(ar.argsort(axis=0))
