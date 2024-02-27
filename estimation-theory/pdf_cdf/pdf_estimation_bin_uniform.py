import numpy as np
import matplotlib.pyplot as plt

from lib.stat import randstat, dataanalysis


randstat.init()

NDATA1 = 100
NDATA2 = 1000
NDATA3 = 10000

NBIN1 = int(np.sqrt(NDATA1))
NBIN2 = int(np.sqrt(NDATA2))
NBIN3 = int(np.sqrt(NDATA3))

data1 = [np.random.normal(0, 1) for i in range(0, NDATA1)]
data2 = [np.random.normal(0, 1) for i in range(0, NDATA2)]
data3 = [np.random.normal(0, 1) for i in range(0, NDATA3)]

trux = np.linspace(-3,3,100)
truy = [np.exp(-x*x / 2.0) / np.sqrt(2.0 * np.pi) for x in trux]


histx1, histy1 = dataanalysis.data2uniformhist1D(data1, NBIN1)
histx2, histy2 = dataanalysis.data2uniformhist1D(data2, NBIN2)
histx3, histy3 = dataanalysis.data2uniformhist1D(data3, NBIN3)

plt.plot(trux, truy)
plt.plot(histx1, histy1)
plt.plot(histx2, histy2)
plt.plot(histx3, histy3)
plt.show()

## CONCLUSION: BINNING IS NOT THE BEST EVER ESTIMATOR OF PDF