# Q-2) Find common elements between A and B. [Hint : Intersection of two sets]

import numpy as np

A=np.array([1,2,3,4,5])
B=np.array([4,5,6,7,8])
C=np.intersect1d(A,B)
print(C)