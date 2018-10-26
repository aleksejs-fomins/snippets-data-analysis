import numpy as np
import matplotlib.pyplot as plt

from aux import randstat, dataanalysis


randstat.init()

NDATA1 = 100
NDATA2 = 1000
NDATA3 = 10000

NDATAPERBIN1 = int(np.sqrt(NDATA1))
NDATAPERBIN2 = int(np.sqrt(NDATA2))
NDATAPERBIN3 = int(np.sqrt(NDATA3))

data1 = [np.random.normal(0, 1) for i in range(0, NDATA1)]
data2 = [np.random.normal(0, 1) for i in range(0, NDATA2)]
data3 = [np.random.normal(0, 1) for i in range(0, NDATA3)]

trux = np.linspace(-3,3,100)
truy = [np.exp(-x*x / 2.0) / np.sqrt(2.0 * np.pi) for x in trux]

histx1, histy1 = dataanalysis.data2nonuniformhist1D(data1, NDATAPERBIN1)
histx2, histy2 = dataanalysis.data2nonuniformhist1D(data2, NDATAPERBIN2)
histx3, histy3 = dataanalysis.data2nonuniformhist1D(data3, NDATAPERBIN3)

plt.plot(trux, truy)
plt.plot(histx1, histy1)
plt.plot(histx2, histy2)
plt.plot(histx3, histy3)
plt.show()

## CONCLUSION: This measure appears to be highly oscillatory