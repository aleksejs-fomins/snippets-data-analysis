import psutil       # System library to get memory use
import h5py         # Write results in HDF5
import numpy as np
import time
import datetime
import matplotlib.pyplot as plt


# def memByProc(thr=1000, nameKey=None):
#     rez = {}
#     for proc in psutil.process_iter():
#         try:
#             #pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
#             key = (proc.pid, proc.name())
#             val = proc.memory_info().vms
#
#             goodName = (nameKey is None) or (nameKey in key[1])
#             if goodName and (val > thr):
#                 rez[key] = val
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass
#     return rez
#
# stuff = memByProc(nameKey='python')



def updateLines(fig, ax, linesCpuUse, x, yarr, scaley=False):
    for line, y in zip(linesCpuUse, yarr):
        line.set_xdata(x)
        line.set_ydata(y)
    ax.set_xlim(x[0], x[-1])
    if scaley:
        ax.set_ylim(np.min(yarr)*0.9, np.max(yarr)*1.1)


timeStep = 0.5           # Seconds, how frequently to update the plot
displayWindow = 100      # How many timesteps to show on a plot

nCpu = psutil.cpu_count()

timeArr = np.array([-timeStep, 0])  # Time since start of measurement
timeTrueArr = np.array([0,0])       # Absolute time
cpuUseArr = np.zeros((nCpu, 2))     # Cpu usage in percent
memUseArr = np.zeros(2)             # Mem usage in bytes

# Initialize plots
plt.ion()
fig, ax = plt.subplots(ncols=2)
ax[0].set_ylim(0, 100)
ax[0].set_title("Cpu Load, %")
ax[1].set_title("Memory Load, Bytes")
linesCpuUse = [ax[0].plot(timeArr, cpuUseArr[i])[0] for i in range(nCpu)]
linesMemUse = [ax[1].plot(timeArr, memUseArr)[0]]

try:
    while True:
        print("time", timeArr[-1])
        cpuPercent = psutil.cpu_percent(percpu=True)

        timeArr = np.append(timeArr, timeArr[-1] + timeStep)
        timeTrueArr = np.append(timeTrueArr, str(datetime.datetime.now().time()))
        cpuUseArr = np.c_[cpuUseArr, np.array(cpuPercent)]
        memUseArr = np.append(memUseArr, psutil.virtual_memory().used)

        updateLines(fig, ax[0], linesCpuUse, timeArr[-displayWindow:], cpuUseArr[:, -displayWindow:])
        updateLines(fig, ax[1], linesMemUse, timeArr[-displayWindow:], [memUseArr[-displayWindow:]], scaley=True)

        fig.canvas.draw()
        fig.canvas.flush_events()

        time.sleep(timeStep)
except:
    print('User closed displayWindow')

print('Writing results to HDF5')
timeArrEncoded = [s.encode("ascii", "ignore") for s in timeTrueArr[2:]]
with h5py.File('perfLog.h5', 'w') as logFile:
    logFile.create_dataset('times', (len(timeArrEncoded), 1), 'S10', data=timeArrEncoded)
    logFile.create_dataset('cpuUse', data=cpuUseArr[:, 2:])
    logFile.create_dataset('memUse', data=memUseArr[2:])

print('Done')
