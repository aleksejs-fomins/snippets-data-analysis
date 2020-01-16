
import multiprocessing

from lib import discretemath, parallel


def computation(args):
    print(args)
    return args[1]

length = 10000
nCore = multiprocessing.cpu_count()
p = multiprocessing.Pool(processes=nCore)

procJobSize = parallel.splitJob(length, nCore)
procStartPosList = discretemath.list_progressive_accumulate(procJobSize[0:length - 1], 0)
procEndPosList = discretemath.list_progressive_accumulate(procJobSize[1:length], procJobSize[0])

p.map(computation, zip(procJobSize, procStartPosList, procEndPosList))