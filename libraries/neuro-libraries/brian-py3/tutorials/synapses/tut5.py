from brian2 import *
import tutorials.synapses.vis_con as vis
start_scope()

N = 10
G = NeuronGroup(N, 'v:1')

for p in [0.1, 0.5, 1.0]:
    S = Synapses(G, G)
    S.connect(condition='i!=j', p=p)
    vis.visualise_connectivity(S)
    suptitle('p = '+str(p))