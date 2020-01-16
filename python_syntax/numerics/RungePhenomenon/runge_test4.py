
import random
import sys

import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as nppoly

sys.path.insert(0, '/home/aleksejs/work/python3/test1/lib/')

from lib.numerics import metrics
from lib.stat import randstat

from pympler.tracker import SummaryTracker
tracker = SummaryTracker()

#################################################################
# This code is designed to test overfitting for polynomial data
#################################################################
# Description

N_TRIALS = 10000    # Total number of random trials
MIN_DIM_POLY = 0    # Lowest dimension of random polynomials
MAX_DIM_POLY = 20   # Highest dimension of random polynomials
MIN_DISCR = 5       # Lowest number of discretization points
MAX_DISCR = 1000    # Highest number of discretization points
MIN_DIM_FIT = 0     # Lowest number of discretization points
MAX_DIM_FIT = 100   # Lowest number of discretization points

MAG_POLY = 2.0      # Magnitude of each initial random polynomial
ERR_DISCR = 0.05    # Standard deviation for normal sampling error




rezDiscrList = []
rezDimList = []

for iTrial in range(0, N_TRIALS):
    print("iTrial=", iTrial)
    DIM_POLY = random.randint(MIN_DIM_POLY, MAX_DIM_POLY)
    N_DISCR = random.randint(MIN_DISCR, MAX_DISCR)

    # Generate a random polynomial and sample it with gaussian errors
    p1 = randstat.URandomPoly(DIM_POLY, MAG_POLY)
    p1sx, p1sy = randstat.samplePoly(p1, N_DISCR, err = ERR_DISCR)

    # Attempt to fit to the sample new polynomials of dimensions 0 to NumberOfDiscretizationPoints
    dimList = [i for i in range(MIN_DIM_FIT, min(N_DISCR+1, MAX_DIM_FIT))]
    l2errList = []
    for iPolyDim in dimList:
         p2 = nppoly.Polynomial.fit(deg=iPolyDim, x=p1sx, y=p1sy)
         l2errList.append(metrics.dist_l2_func_1D(p1, p2, 0, 1))

    rezDiscrList.append(N_DISCR)
    rezDimList.append(discretemath.argmin(dimList, l2errList)[0])


print(rezDiscrList)
print(rezDimList)

plt.plot(rezDiscrList, rezDimList, "o")
plt.show()

tracker.print_diff()


# 4) Progressively L2-fit to the sample a set of polynomials with increasing dimension
# 5) Calculate the L2-integral error between original and fitted polynomial (continuous)
# 6) Determine dimension Dmin(M,N,s) with the smallest integral error
# 7) Repeat for different M,N,s. Draw empirical rule of thumb.