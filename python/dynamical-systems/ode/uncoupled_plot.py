import numpy as np
import matplotlib.pyplot as plt
from uncoupled_lib import UncoupledOscillators            

osc = UncoupledOscillators(10, 0.001, 1, 5)
x, v = osc.run(100000)
KE = np.multiply(osc.w2, x**2)/2 + v**2/2


fig, ax = plt.subplots(ncols=3, figsize=(12,4))
ax[0].plot(x)
ax[1].plot(v)
ax[2].plot(KE)
#ax[2].plot(np.average(KE, axis=1))
plt.show()
