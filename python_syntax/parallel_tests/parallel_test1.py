import time

import matplotlib.pyplot as plt

from lib import parallel

nTask = [i ** 2 for i in range(1, 100)]
nTime = []

for iReal in nTask:
    print(iReal)
    start = time.time()
    rez = parallel.serial_series((parallel.numeric_time_killer1, 1, iReal))
    end = time.time()
    nTime.append(end - start)

plt.plot(nTask, nTime)
plt.show()