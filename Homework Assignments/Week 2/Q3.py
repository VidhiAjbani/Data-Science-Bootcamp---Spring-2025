# Q-3) Extract all numbers from A which are within a specific range. eg between 5 and 10. [Hint: np.where() might be useful or boolean masks]

import numpy as np

A=np.array([1,2,3,4,5])
b_mask=(A<5) & (A>2)
C=A[b_mask]
print(C)