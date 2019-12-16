'''
Test if multiprocessing.pool.map leaks anything until program is closed.

Answer: No, memory freed up completely after pool is closed

'''

import time
import numpy as np
import pathos, multiprocessing

def hardTest():
    tasks = np.arange(100)
    bigArray = np.zeros(100000000)

    def func(i, data):
        print("Proc", multiprocessing.current_process().pid, "doing task", i)
        return np.sum(data[i:])

    fwrapper = lambda i: func(i, bigArray)

    pool = pathos.multiprocessing.ProcessingPool(4)
    pool.map(fwrapper, tasks)


for iTest in range(5):
    hardTest()
    print('Finished test', iTest)
    time.sleep(2)