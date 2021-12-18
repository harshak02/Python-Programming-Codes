import numpy as np
#do same like strings logic :
#attributes and functions...In functions only we can take axis=x
#for attributes pls do write as print(array.xxxx) directly or can be written
#as the string logics also
#from reshape onwards we need to write as like strings logic


#___________________Introduction______________________:

myarr = np.array([1,2,3,4,5])
print(myarr)

#________________accessing any element_________________:

print(myarr[3])

#________________here 1D array means____________________:

print(myarr[0])

#________________here 2D array mean_____________________:


myarr2 = np.array([[1,2,3,4],[5,6,7,8]])
print(myarr2)
print(myarr2[1,0])#returns the 2nd array 1st element
print(myarr2[0,1])#returns the 1st array 1st element

#_________________memory assigning_______________________:


myarr3 = np.array([1,2,3,4],np.int8)
#sets all the integer memory to one byte i.e 8 bytes  
print(myarr3)


#__________________shape of array________________________:


print(myarr.shape)
#gives (5,)-> 5 columns and 1 row

myarr4 = np.array([[1,2],[4,5,6]])
print(myarr4.shape)
#gives (2,) coz no.of coloumns are uncertain

print(myarr2.shape)
#gives (2,4) coz no.of coloumns are 4 common in both rows


#_____________________dtypeCodes_________________________:

print(myarr.dtype)
#default is int32 
print(myarr3.dtype)



