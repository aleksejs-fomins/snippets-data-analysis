from aan import network

import numpy as np
import matplotlib.pyplot as plt


n1 = network.AAN([1,2,3])

x = np.linspace(-10, 10, 100)
y = n1.sigmoid(x)
plt.plot(x, y)
plt.show()