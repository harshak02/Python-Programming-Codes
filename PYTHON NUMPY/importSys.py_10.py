import sys
import numpy as np 

py_ar = [1,2,3,4,5]
np_ar = np.array(py_ar)

size1 = sys.getsizeof(1)*len(py_ar)
print(size1)

size2 = np_ar.itemsize * np_ar.size
print(size2)

#so you can see the difference

'''use :-
scipy.org for any reference'''
