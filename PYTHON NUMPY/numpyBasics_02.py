import numpy as np

myarr = np.array([[1,2,3,4]],np.int16)

print(myarr[0,1])
print(myarr[0])#used only for 1D generally but
#2D means gives whole array

#__________________changing Values________________________:

myarr[0,1]=45
print(myarr)

# myarr[0] = [9,8,7,6,5]->throws error
# print(myarr)

myarr[0] = [9,8,7,6]
print(myarr)#same size is prefered



