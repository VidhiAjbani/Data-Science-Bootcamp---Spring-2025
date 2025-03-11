# Q-1) Define two custom numpy arrays, say A and B. Generate two new numpy arrays by stacking A and B vertically and horizontally.

import numpy as np

A=np.array([1,2,3,4,5])
B=np.array([4,5,6,7,8])
C=np.vstack((A,B))
print(C)