import numpy as np
import matplotlib.pyplot as plt

from lib.stat import randstat, dataanalysis, infotheory_sample


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

histx1, histy1 = dataanalysis.data2uniformhist1D(data1, NBIN1)
histx2, histy2 = dataanalysis.data2uniformhist1D(data2, NBIN2)
histx3, histy3 = dataanalysis.data2uniformhist1D(data3, NBIN3)

width1 = [(max(data1) - min(data1)) / NBIN1] * NBIN1
width2 = [(max(data2) - min(data2)) / NBIN2] * NBIN2
width3 = [(max(data3) - min(data3)) / NBIN3] * NBIN3

shannonH1 = infotheory_sample.shannonEntropy1Dbin(width1, histy1)
shannonH2 = infotheory_sample.shannonEntropy1Dbin(width2, histy2)
shannonH3 = infotheory_sample.shannonEntropy1Dbin(width3, histy3)

print(shannonH1)
print(shannonH2)
print(shannonH3)