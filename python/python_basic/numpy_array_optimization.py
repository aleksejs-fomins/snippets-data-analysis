import time
import numpy as np
from matplotlib import pyplot as plt

'''
    Conclusions:
      1) Python makes dramatic optimization of np.array() addition. It is much better than 
      2) np.sum() is dramatically better than sum() in certain scenarios
      3) there is a memory allocation time penalty for np.array(). There seems to be an optimal size (1000000 elem?),
         beyond which memory penalty is more expensive than optimization gain 
'''

def Gaussian(X, Y, x, y):
    return np.exp(-(X-x)**2 - (Y-y)**2)

XMid = 0.0
YMid = 0.0
XSig = 1.0
YSig = 1.0
NStep = 100
EXTENT = [-1, 1, -1, 1]
PX = np.arange(EXTENT[0], EXTENT[1], (EXTENT[1] - EXTENT[0]) / NStep)
PY = np.arange(EXTENT[2], EXTENT[3], (EXTENT[3] - EXTENT[2]) / NStep)
PXm, PYm = np.meshgrid(PX, PY)

NRandList = list(range(100, 10000, 200))
Timings1 = []
Timings2 = []
Timings3 = []
Timings4 = []
Timings5 = []

for NRand in NRandList:
    XX = np.random.normal(XMid, XSig, NRand)
    YY = np.random.normal(YMid, YSig, NRand)

    # ''' 3D Loop, no extra structures. 800 Seconds '''
    # start1 = time.time()
    # rez = np.zeros((NStep, NStep))
    # for i in range(NStep):
    #     for j in range(NStep):
    #         for k in range(NRand):
    #             rez[i][j] += Gaussian(XX[k], YY[k], PX[i], PY[j])
    # end1 = time.time()
    #
    # ''' 2D Loop, np.array operations on 1D arrays. 34.6 Seconds '''
    # start2 = time.time()
    # rez = np.zeros((NStep, NStep))
    # for i in range(NStep):
    #     for j in range(NStep):
    #         rez[i][j] = sum(Gaussian(XX, YY, PX[i], PY[j]))
    # end2 = time.time()

    # ''' 1D Loop, np.array operations on 3D arrays. 11.9 Seconds '''
    # start3 = time.time()
    # rez = np.sum(Gaussian(XX[:, None, None], YY[:, None, None], PXm, PYm), axis=0)
    # end3 = time.time()

    # ''' 2D Loop, np.array operations on 1D arrays. Extra list conversion. 9.2 Seconds '''
    # start4 = time.time()
    # rez = np.array([[np.sum(Gaussian(XX, YY, x, y)) for y in PY] for x in PX])
    # end4 = time.time()
    #
    # ''' 1D Loop, np.array operations on 3D arrays. 11.9 Seconds '''
    # start5 = time.time()
    # # rez = np.sum(np.array([Gaussian(XX[i], YY[i], PXm, PYm) for i in range(NRand)]), axis=0)
    # rez = np.zeros((NStep, NStep))
    # for i in range(NRand):
    #     rez += Gaussian(XX[i], YY[i], PXm, PYm)
    # end5 = time.time()

    # Timings1.append(end1 - start1)
    # Timings2.append(end2 - start2)
    # Timings3.append(end3 - start3)
    # Timings4.append(end4 - start4)
    # Timings5.append(end5 - start5)
    # print(NRand)
    # print(Timings4[len(Timings4) - 1])
    # print(Timings5[len(Timings5) - 1])


# print(rez.shape)
# plt.imshow(rez, cmap='jet', interpolation='nearest', origin='lower', extent=EXTENT)
# plt.show()

# plt.plot(NRandList, Timings1)
# plt.plot(NRandList, Timings2)
# plt.plot(NRandList, Timings3)
# plt.plot(NRandList, Timings4)
# plt.plot(NRandList, Timings5)
# plt.show()