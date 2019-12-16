import multiprocessing

import numpy as np

from lib import discretemath


# Some operation that takes time
def numeric_time_killer1(x):
    rez = 0.0
    for i in range(1, 10):
        rez += np.log(i*x)
    return rez


# Split job as uniformly as possible among multiple cores
def splitJob(nTotJob, nCore):
    rez = []
    for i in range(nCore, 0, -1):
        thisSize = int(np.ceil(nTotJob / i))
        rez.append(thisSize)
        nTotJob -= thisSize
    return rez


# A serial code that calls a function for a list
# of integer values, returning a list of all results
def serial_series(args):
    f, iMin, iMax = args
    return [f(i) for i in range(iMin, iMax)]


def parallel_series(args):
    f, iMin, iMax, nCore = args

    length = iMax - iMin

    #print('ZZZ', nCore, iMin, iMax)

    procJobFunction = [f] * nCore
    procJobSize = splitJob(length, nCore)
    procStartPosList = discretemath.list_progressive_accumulate(procJobSize[0:length - 1], iMin)
    procEndPosList = discretemath.list_progressive_accumulate(procJobSize[1:length], procJobSize[0] + 1)

    #print(procJobSize, procStartPosList, procEndPosList)

    pool = multiprocessing.Pool(processes=nCore)
    rez = pool.map(serial_series, zip(procJobFunction, procStartPosList, procEndPosList))
    #rezSpawn = pool.apply_async(serial_series, zip(procJobFunction, procStartPosList, procEndPosList))

    pool.terminate()
    pool.join()

    #pool.close()
    #pool.join()

    #rez = rezSpawn.get()
    #print(rez)

    # Reduce list of lists
    return [item for rezProc in rez for item in rezProc]
    #return rez









