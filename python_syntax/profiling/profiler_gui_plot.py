import h5py
import matplotlib.pyplot as plt
import numpy as np

def str2seconds(s):
    h,m,s = [float(t) for t in s.split(':')]
    return s + m * 60 + h * 3600

with h5py.File('perfLog.h5', 'r') as logFile:
    timesEnc = np.copy(logFile['times'])
    cpuUseArr = np.copy(logFile['cpuUse'])
    memUseArr = np.copy(logFile['memUse'])

    print(timesEnc.shape)
    print(cpuUseArr.shape)
    print(memUseArr.shape)

# Decode times
times = [t[0].decode("ascii", "ignore") for t in timesEnc]
timesSec = np.array([str2seconds(s) for s in times])
timesSec -= timesSec[0]


fig, ax = plt.subplots(ncols=2)
ax[0].set_title("Cpu Load, %")
ax[1].set_title("Memory Load, Bytes")
linesCpuUse = [ax[0].plot(timesSec, cpuUse)[0] for cpuUse in cpuUseArr]
linesMemUse = [ax[1].plot(timesSec, memUseArr)[0]]
plt.show()