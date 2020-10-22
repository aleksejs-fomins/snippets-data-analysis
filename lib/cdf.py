import numpy as np

class SampleCDF():
    def __init__(self, data1D):
        self.nData = data1D.shape[0]
        self.pArr = np.linspace(0, 1, self.nData)
        self.xArr = np.sort(data1D)

    def getP(self):
        return np.copy(self.pArr)

    def getX(self):
        return np.copy(self.xArr)

    # Evaluate empirical CDF at point x
    def eval(self, x):
        idx = np.searchsorted(self.xArr, x)
        return self.pArr[idx]

    # Evaluate inverse empirical CDF at probability p
    def inv(self, p):
        dataIdxs = np.clip(p * self.nData, 0, self.nData - 1).astype(int)
        return self.xArr[dataIdxs]
