
from scipy.stats import hypergeom, binom
import matplotlib.pyplot as plt
import numpy as np

# N = Na + Nb  # Number of objects in the pile
# n = na + nb  # Number of objects we will pick
N = 100
Na = 30
n = 12


na = np.arange(0, n + 1)
b_pmf = binom.pmf(na, n, Na/N)
h_pmf = hypergeom(N, Na, n).pmf(na)

print(b_pmf)
print(h_pmf)

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(na, pmf_dogs, 'bo')
# ax.vlines(na, 0, pmf_dogs, lw=2)
# ax.set_xlabel('# of dogs in our group of chosen animals')
# ax.set_ylabel('hypergeom PMF')
# plt.show()

