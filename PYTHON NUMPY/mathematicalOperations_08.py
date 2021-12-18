import numpy as np

ar = np.array([[1,2,3],[4,5,6],[7,1,0]])
ar2 = np.array([[1,2,1],[4,0,6],[8,1,0]])

print(ar+ar2)
#but if we use list then list will get extended but elements wont get added

print(ar*ar2)

ar3 = np.sqrt(ar)#can alos take arguments like an array itself
print(ar3)

#here we use np.soemthing when we are creating an array new or from others


print(ar.sum())
print(ar.min())
print(ar.max())
