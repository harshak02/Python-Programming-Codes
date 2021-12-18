import numpy as np

#method 2 :

zeros = np.zeros((2,5))
print(zeros)

rng = np.arange(15)
print(rng)

lspace = np.linspace(1,50,10)
print(lspace)
#here the 1 is lower limit and 50 is higher limit and 10 is the no. of numbers

emp = np.empty((4,6))
print(emp)
#fills the array with the random numbers 


emp_like = np.empty_like([1,2,3,4])
print(emp_like)
#copies size and gives random values

ide = np.identity(45)
print(ide)
#contains n-Dim arrays
#gives diagonal matrix with 45 as diagonal lenght
print(ide.shape)


arr = np.arange(98) 
