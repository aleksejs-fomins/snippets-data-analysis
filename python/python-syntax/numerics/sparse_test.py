import random
import numpy as np
from scipy.sparse import csr_matrix

x = np.array([0,1,2,3,4])
y = (x + 1) % 5
val = np.random.uniform(0, 1, 5)

M = csr_matrix((val, (x, y)), shape=(5, 5), dtype=float)

print(M.toarray())

print(M.tocoo().row)
print(M.tocoo().col)

print(M.shape)
print(M.dtype)