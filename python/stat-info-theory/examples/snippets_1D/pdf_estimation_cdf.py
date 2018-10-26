import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as nppoly

from aux import randstat, dataanalysis


randstat.init()

data1 = [np.random.normal(0, 1) for i in range(0, 10)]
data2 = [np.random.normal(0, 1) for i in range(0, 100)]
data3 = [np.random.normal(0, 1) for i in range(0, 10000)]

cdfx1, cdfy1 = dataanalysis.cdf1d(data1)
cdfx2, cdfy2 = dataanalysis.cdf1d(data2)
cdfx3, cdfy3 = dataanalysis.cdf1d(data3)

p3 = nppoly.Polynomial.fit(deg=15, x=cdfx3, y=cdfy3)
p3d = p3.deriv()
p3sx1, p3sy1 = randstat.samplePoly(p3, 1000, err = 0.0, left=min(cdfx3), right=max(cdfx3))
p3dsx1, p3dsy1 = randstat.samplePoly(p3d, 1000, err = 0.0, left=min(cdfx3), right=max(cdfx3))


plt.plot(cdfx1, cdfy1)
plt.plot(cdfx2, cdfy2)
plt.plot(cdfx3, cdfy3)
plt.plot(p3sx1, p3sy1)
#plt.plot(p3dsx1, p3dsy1)
plt.show()

## CONCLUSION: CDF estimator actually is even worse than bin, since
##  derivative of a fitted function is very sensitive to data.
##  Also, special functions may be needed to have 0 derivative of CDF on the boundaries