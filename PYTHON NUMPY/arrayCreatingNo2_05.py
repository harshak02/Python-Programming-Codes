import numpy as np

arr = np.arange(99)
print(arr)

arr1 = arr.reshape(3,33)#imp same as strings
#here the arguments product should be 99->throws no error
print(arr)

arr2 = arr1.ravel()#reverse of reshape

print(arr2)
print(arr2.shape)
