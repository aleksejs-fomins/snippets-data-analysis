import time
import numpy as np
import multiprocessing
import matplotlib.pyplot as plt


def foo(x):
    return sum([np.log(1 + i*x) for i in range(10)])


def serial_series(rangeMax):
    return [foo(i) for i in range(rangeMax)]

def parallel_series_1core(rangeMax):
    pool = multiprocessing.Pool(processes=1)
    #rez = pool.map(foo, tuple(range(rangeMax)))
    rez = pool.map(serial_series, [rangeMax])

    pool.terminate()
    pool.join()

    return rez


nTask = [1 + i ** 2 * 1000 for i in range(1, 20)]
nTimeSerial = []
nTimeParallel = []

for taskSize in nTask:
    print('TaskSize', taskSize)
    start = time.time()
    rez1 = serial_series(taskSize)
    #print(rez1)
    end = time.time()
    nTimeSerial.append(end - start)

#for taskSize in nTask:
    #print('TaskSize', taskSize)
    start = time.time()
    rez2 = parallel_series_1core(taskSize)
    #print(rez2)
    end = time.time()
    nTimeParallel.append(end - start)


plt.plot(nTask, nTimeSerial)
plt.plot(nTask, nTimeParallel)
plt.plot(nTask, [float(i) / j for i,j in zip(nTimeParallel, nTimeSerial)])

plt.legend(['serial', 'parallel 1 core', 'ratio'])
plt.show()