
from scipy.stats import hypergeom, binom
import matplotlib.pyplot as plt
import numpy as np

# N = Na + Nb  # Number of objects in the pile
# n = na + nb  # Number of objects we will pick
Nmin = 40
Nmax = 1000
p = 1.0/3.0
n = 10
na = 3

N = np.arange(Nmin, Nmax+1)
Na = (p * N).astype(int)

b_pmf = binom.pmf(na, n, Na/N)
h_pmf = hypergeom(N, Na, n).pmf(na)

print(b_pmf)
print(h_pmf.shape)

plt.plot(N, b_pmf, label="binom")
plt.plot(N, h_pmf, label="hyper")
plt.legend()
plt.show()