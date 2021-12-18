import numpy

list2 = list(map(int,input().strip().split()))

valAt = input()
valAt = int(valAt)


print (numpy.polyval(list2,valAt))


#in numpy we have all related to maths and polynomials