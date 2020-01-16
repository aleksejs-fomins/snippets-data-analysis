
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as nppoly

from lib.numerics import metrics
from lib.stat import randstat

#################################################################
# This code is designed to test overfitting for polynomial data
#################################################################
# Description

N_POLY = 10         # Number of initial random polynomials
DIM_POLY = 3        # Dimension of each initial random polynomial
MAG_POLY = 2.0      # Magnitude of each initial random polynomial
N_DISCR = 20        # Number of discretization points of the domain
ERR_DISCR = 0.05    # Standard deviation for normal sampling error


for iPoly in range(0, N_POLY):
    # Generate a random polynomial and sample it with gaussian errors
    p1 = randstat.URandomPoly(DIM_POLY, MAG_POLY)
    p1sx, p1sy = randstat.samplePoly(p1, N_DISCR, err = ERR_DISCR)

    # Attempt to fit to the sample new polynomials of dimensions 0 to NumberOfDiscretizationPoints
    dimList = [i for i in range(0, N_DISCR+1)]
    l2errList = []
    for iPolyDim in dimList:
        p2 = nppoly.Polynomial.fit(deg=iPolyDim, x=p1sx, y=p1sy)
        l2errList.append(metrics.dist_l2_func_1D(p1, p2, 0, 1))

    plt.semilogy(dimList, l2errList)

plt.show()