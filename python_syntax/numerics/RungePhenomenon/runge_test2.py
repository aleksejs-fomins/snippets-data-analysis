
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as nppoly

from lib.stat import randstat

DIM_POLY = 3        # Dimension of the initial random polynomial
MAG_POLY = 2.0      # Magnitude of the initial random polynomial
N_DISCR = 20        # Number of discretization points of the domain
ERR_DISCR = 0.05    # Standard deviation for normal sampling error

# Generate random polynomial and sample it
p1 = randstat.URandomPoly(DIM_POLY, MAG_POLY)
p1sx1, p1sy1 = randstat.samplePoly(p1, N_DISCR, err = 0.0)

# Also sample that polynomial with gaussian error
p1sx2, p1sy2 = randstat.samplePoly(p1, N_DISCR, err = ERR_DISCR)

# Fit a new polynomial of the same degree to the sample, and sample new polynomial
p2 = nppoly.Polynomial.fit(deg=DIM_POLY, x=p1sx2, y=p1sy2)
p2sx1, p2sy1 = randstat.samplePoly(p2, N_DISCR, err = 0.0)

# Plot everything
plt.plot(p1sx1, p1sy1)
plt.plot(p1sx2, p1sy2)
plt.plot(p2sx1, p2sy1)
plt.show()