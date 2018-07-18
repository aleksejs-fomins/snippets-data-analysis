from brian2 import *
import tutorials.synapses.vis_con as vis
start_scope()

N = 10
G = NeuronGroup(N, 'v:1')
S = Synapses(G, G)
S.connect(condition='i!=j', p=0.2)


import tutorials.synapses.vis_con as vis
vis.visualise_connectivity(S)