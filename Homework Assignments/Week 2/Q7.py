# Q-7) How to get the rows of a dataframe with row sum > 100?

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
r=df.sum(axis=1)
rows=df[r>100]
print(rows)