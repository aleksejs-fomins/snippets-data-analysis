import matplotlib.pyplot as plt

from lib.stat import randstat

randstat.init()

DIM_POLY = 3        # Dimension of the initial random polynomial
MAG_POLY = 2.0      # Magnitude of the initial random polynomial
N_DISCR = 20        # Number of discretization points of the domain
ERR_DISCR = 0.03    # Standard deviation for normal sampling error
N_POLY = 10         # Number of random samples

# Generate and plot the random polynomial
p1 = randstat.URandomPoly(DIM_POLY, MAG_POLY)
xList, yList = randstat.samplePoly(p1, N_DISCR, 0)
plt.plot(xList, yList)

# Sample the polynomial randomly and plot piecewise-continuous result
for i in range(0, N_POLY):
    xList, yList = randstat.samplePoly(p1, N_DISCR, ERR_DISCR)
    plt.plot(xList, yList)

plt.show()

