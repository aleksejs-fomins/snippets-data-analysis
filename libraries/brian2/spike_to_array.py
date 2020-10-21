import numpy as np
import matplotlib.pyplot as plt
from time import time

from brian2 import start_scope, NeuronGroup, Synapses, ms, Hz, run, SpikeMonitor, PoissonGroup

def time_me(func):
    def wrapper(*args, **kwargs):
        t = time()
        print("Started", func.__name__)
        rez = func(*args, **kwargs)
        print("Finished", func.__name__, "in", time() - t)
        return rez
    return wrapper

@time_me
def simulate(nNeurons=100, simTime=50):
    start_scope()

    P = PoissonGroup(nNeurons, 100*np.arange(nNeurons) * Hz + 1000 * Hz)
    G = NeuronGroup(nNeurons, 'dv/dt = -v / (10*ms) : 1', threshold='v>1', reset='v = 0', method='exact')
    S = Synapses(P, G, on_pre='v+=0.1')
    S.connect(j='i')

    M = SpikeMonitor(G, variables='v')

    run(simTime*ms)

    return M


@time_me
def spike_times_to_matrix(spikeMon, nX, nY, startTime, endTime, nBins):
    rezArr = np.zeros((nX, nY, nBins))
    tStep = float((endTime - startTime) / nBins)

    coord1Dto2D = lambda i: (i // nY, i % nY)
    time2bin = lambda t: int((t - startTime) / tStep)

    for iNeuron, tList in spikeMon.all_values()['t'].items():
        x, y = coord1Dto2D(iNeuron)
        for t in tList:
            bin = time2bin(t)
            rezArr[x, y, bin] += 1

    return rezArr

nX = 10
nY = 10
simTime = 100
M = simulate(nNeurons=nX*nY, simTime=simTime)

arr = spike_times_to_matrix(M, nX, nY, 0*ms, simTime*ms, 2)

plt.figure()
plt.imshow(arr[:,:,-1])
plt.show()
