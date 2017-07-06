import numpy as np
import joblib
import time
import matplotlib.pyplot as plt

def foo(x):
    return np.log(x+1)

def comp_parallel(f, nCore, rangeMax):
    x = range(0, rangeMax)
    return joblib.Parallel(n_jobs=nCore)(joblib.delayed(f)(i) for i in x)


nCore = range(1,9)
tRun = []

for iCore in nCore:
    t_begin = time.time()
    comp_parallel(foo, iCore, 100000)
    t_end = time.time()
    tRun.append(t_end - t_begin)

plt.plot(nCore, tRun)
plt.show()
