
from scipy.stats import hypergeom, binom
import matplotlib.pyplot as plt
import numpy as np

Nmin = 40       # Number of cards in deck
Nmax = 100
p = 1.0/3.0     # Proportion of lands
n = 10          # Number of cards drawn
na = np.arange(0, n + 1)


b_pmfs = []
h_pmfs = []

for N in range(Nmin, Nmax+1):
    Na = int(p * N)
    b_pmfs.append(binom.pmf(na, n, Na/N))
    h_pmfs.append(hypergeom(N, Na, n).pmf(na))

b_pmfs = np.array(b_pmfs)
h_pmfs = np.array(h_pmfs)


fig = plt.figure()
b_fig = fig.add_subplot(1,3,1)
b_imgplot = plt.imshow(b_pmfs, extent=[0,n,Nmax, Nmin])
b_fig.set_title('Binomial')
plt.colorbar(orientation ='horizontal')

h_fig = fig.add_subplot(1,3,2)
h_imgplot = plt.imshow(h_pmfs, extent=[0,n,Nmax, Nmin])
h_fig.set_title('Hypergeometric')
plt.colorbar(orientation='horizontal')

d_fig = fig.add_subplot(1,3,3)
d_imgplot = plt.imshow(np.abs(h_pmfs - b_pmfs), extent=[0,n,Nmax, Nmin])
d_fig.set_title('Difference')
plt.colorbar(orientation='horizontal')

plt.show()