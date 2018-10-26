'''
    Attempt to cluster two overlapping gaussians by analysing a heatmap
    of a sum of different loss functions over all points, progressively
    decreasing the temperature (variance) of each loss function

    TODO: PLOT CONTOUR LINES NEXT TO THE PEAK, SEE HOW THEY BEHAVE,
'''

from python.aux import randstat, moments
import numpy as np
from matplotlib import pyplot as plt

randstat.init()

def randball(com, sig, n):
    X = np.random.normal(com[0], sig, n)
    Y = np.random.normal(com[1], sig, n)
    return X, Y

def phi(px, py, X, Y, rthresh=1.0):
    rad = np.sqrt((X - px)**2 + (Y - py)**2)
    Nrm = np.where(rad < rthresh, np.sqrt(1.0 / rthresh), np.sqrt(1.0 / rad))
    return Nrm

def gausqrt(px, py, X, Y, sig=10):
    rad = np.sqrt((X - px)**2 + (Y - py)**2)
    return np.exp(-rad / sig)

def lorentz(px, py, X, Y, sig2=100):
    rad2 = (X - px)**2 + (Y - py)**2
    return 1.0 / (rad2 + sig2)

NRandPoint = 200
X1,Y1 = randball([5, 5], 5, int(NRandPoint/2))
X2,Y2 = randball([-5,-5], 5, int(NRandPoint/2))
X = np.array(list(X1) + list(X2))
Y = np.array(list(Y1) + list(Y2))

avgx = moments.avg(X)
avgy = moments.avg(Y)
sig2x = moments.sig2(X, avgx)
sig2y = moments.sig2(Y, avgy)
sig2 = sig2x + sig2y
print("sig2=", sig2)

NSTEP = 500
extent = [-10, 10, -10, 10]
PX = np.linspace(extent[0], extent[1], NSTEP)
PY = np.linspace(extent[2], extent[3], NSTEP)
PXm, PYm = np.meshgrid(PX, PY)



for sig2 in range(50, 0, -1):
    print(sig2)
    PZ = np.zeros((NSTEP, NSTEP))
    for i in range(NRandPoint):
        # PZ += gausqrt(PXm, PYm, X[i], Y[i], sig=np.sqrt(sig2))
        PZ += lorentz(PXm, PYm, X[i], Y[i], sig2=sig2)

    print(PZ.shape)
    #plt.scatter(X, Y)
    plt.imshow(PZ, interpolation='nearest', origin='lower', extent=extent)
    plt.savefig("figs/fig"+str(sig2)+".png")
    #plt.show()
